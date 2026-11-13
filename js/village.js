/* Homepage: village hotspots, orange tree, countdown, scroll into the story map. */
(function () {
  'use strict';

  var hero = document.querySelector('.hero');
  var picture = document.querySelector('.picture');
  var scroller = document.querySelector('.hero-scroll');
  var spots = Array.prototype.slice.call(document.querySelectorAll('.go'));
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Hotspots: hover/tap shows the label, click walks in ---------- */

  var lastPointer = 'mouse';
  document.addEventListener('pointerdown', function (e) { lastPointer = e.pointerType; }, true);

  function closeAll(except) {
    spots.forEach(function (s) { if (s !== except) s.classList.remove('open'); });
  }

  function walkIn(spot) {
    var href = spot.getAttribute('href');
    if (reduceMotion) { location.href = href; return; }
    var h = hero.getBoundingClientRect();
    var b = spot.getBoundingClientRect();
    hero.style.setProperty('--ox', (b.left + b.width / 2 - h.left) + 'px');
    hero.style.setProperty('--oy', (b.top + b.height / 2 - h.top) + 'px');
    spot.classList.add('open');
    document.body.classList.add('entering');
    setTimeout(function () { location.href = href; }, 850);
  }

  spots.forEach(function (spot) {
    spot.addEventListener('click', function (e) {
      if (spot.dataset.held) { e.preventDefault(); delete spot.dataset.held; return; }   // a long press already did its thing
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;   // new tab etc.
      e.preventDefault();
      // Touch has no hover: first tap shows the label (and opens a door), second tap goes in
      if (lastPointer === 'touch' && !spot.classList.contains('open')) {
        closeAll(spot);
        spot.classList.add('open');
        return;
      }
      walkIn(spot);
    });
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.go')) closeAll(null); });
  window.addEventListener('pageshow', function () {
    document.body.classList.remove('entering');
    closeAll(null);
  });

  /* ---------- Weathervane: press and hold → it points to where you are ----------
     A normal click still opens the guest map. Holding asks (once) for the
     visitor's location, turns the arrow from Tavira towards them and tells
     them how far away Tavira is. Nothing is stored or sent anywhere. */

  var TAVIRA = { lat: 37.1273, lon: -7.6486 };
  var vane = document.querySelector('.vane');
  var vaneArrow = vane.querySelector('.vane-arrow');
  var holdTimer = null, homeTimer = null;

  function toRad(d) { return d * Math.PI / 180; }
  function distanceKm(a, b) {
    var dLat = toRad(b.lat - a.lat), dLon = toRad(b.lon - a.lon);
    var h = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(toRad(a.lat)) * Math.cos(toRad(b.lat)) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
    return 6371 * 2 * Math.asin(Math.sqrt(h));
  }
  function bearing(a, b) {                       // initial great-circle bearing from a to b, degrees from north
    var y = Math.sin(toRad(b.lon - a.lon)) * Math.cos(toRad(b.lat));
    var x = Math.cos(toRad(a.lat)) * Math.sin(toRad(b.lat)) -
            Math.sin(toRad(a.lat)) * Math.cos(toRad(b.lat)) * Math.cos(toRad(b.lon - a.lon));
    return (Math.atan2(y, x) * 180 / Math.PI + 360) % 360;
  }
  function compassWord(deg) {
    return ['north', 'north-east', 'east', 'south-east', 'south', 'south-west', 'west', 'north-west'][Math.round(deg / 45) % 8];
  }

  function pointHome() {
    var say = window.toast || function () {};
    if (!navigator.geolocation) { say('Wherever you are, the Algarve is waiting for you.'); return; }
    say('Finding your way to Tavira…', 2500);
    navigator.geolocation.getCurrentPosition(function (pos) {
      var you = { lat: pos.coords.latitude, lon: pos.coords.longitude };
      var km = distanceKm(TAVIRA, you);
      var toYou = bearing(TAVIRA, you);          // the arrow (standing in Tavira) points towards you
      var toTavira = bearing(you, TAVIRA);
      // rotateY: 0° = arrow head east, +90° = head away from us (north), so turn = 90° − bearing
      var turn = 90 - toYou;
      vaneArrow.classList.add('pointing');
      vaneArrow.style.setProperty('--turn', (turn + 720) + 'deg');
      var msg;
      if (km < 25) msg = 'You’re already in Tavira! See you at the long table.';
      else {
        var nice = km < 100 ? Math.round(km) : Math.round(km / 10) * 10;
        msg = 'You’re ' + nice.toLocaleString('en-GB') + ' km from Tavira. Head ' + compassWord(toTavira) + ' – we’ll keep a seat for you.';
        if (km > 500) msg += ' (About ' + Math.max(1, Math.round((km / 800 + .5) * 2) / 2) + ' h by plane.)';
      }
      say(msg, 7000);
      clearTimeout(homeTimer);
      homeTimer = setTimeout(function () {
        vaneArrow.classList.remove('pointing');
        vaneArrow.style.removeProperty('--turn');
      }, 9000);
    }, function () {
      say('No problem – wherever you are, the Algarve is waiting for you.', 4500);
    }, { enableHighAccuracy: false, timeout: 10000, maximumAge: 600000 });
  }

  vane.addEventListener('pointerdown', function () {
    delete vane.dataset.held;
    clearTimeout(holdTimer);
    vane.classList.add('holding');
    holdTimer = setTimeout(function () {
      vane.dataset.held = '1';
      vane.classList.remove('holding');
      pointHome();
    }, 650);
  });
  ['pointerup', 'pointerleave', 'pointercancel'].forEach(function (ev) {
    vane.addEventListener(ev, function () { clearTimeout(holdTimer); vane.classList.remove('holding'); });
  });
  vane.addEventListener('contextmenu', function (e) { e.preventDefault(); });   // no long-press menu on phones

  /* ---------- Street lamp: switches day / night ---------- */

  var root = document.documentElement;
  var lamp = document.querySelector('.lamp');
  var lampTip = lamp.querySelector('.tip');
  function syncLamp() {
    var night = root.dataset.theme === 'night';
    lampTip.textContent = night ? 'Turn off the lamp' : 'Light the lamp';
    lamp.setAttribute('aria-label', night ? 'Turn off the street lamp (day mode)' : 'Light the street lamp (night mode)');
    lamp.setAttribute('aria-pressed', String(night));
  }
  lamp.addEventListener('click', function () {
    window.setTheme(root.dataset.theme === 'night' ? 'day' : 'night');
  });
  new MutationObserver(syncLamp).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
  syncLamp();

  /* ---------- Orange tree ---------- */

  var shaken = 0;
  document.querySelector('.tree').addEventListener('click', function () {
    shaken++;
    if (shaken === 10 && window.toast) {
      window.toast('That’s enough for a glass of fresh orange juice. See you in Tavira!', 5000);
    }
    var o = document.createElement('span');
    var x = 500 + Math.random() * 230;        // canopy, picture pixels
    var y = 300 + Math.random() * 170;
    o.className = 'orange';
    o.style.left = (x / 1926 * 100) + '%';
    o.style.top = ((y + 360) / 1177 * 100) + '%';
    o.style.setProperty('--floor', ((690 + Math.random() * 25 + 360) / 1177 * 100) + '%');
    o.style.setProperty('--roll', ((Math.random() < .5 ? -1 : 1) * (15 + Math.random() * 50)) + 'px');
    o.style.setProperty('--dur', (0.55 + (700 - y) / 700).toFixed(2) + 's');
    picture.appendChild(o);
    setTimeout(function () { o.remove(); }, 4500);
  });

  /* ---------- Countdown ---------- */

  var cd = document.getElementById('countdown');
  var now = new Date();
  var days = Math.ceil((new Date(2027, 9, 1) - now) / 864e5);
  cd.textContent = days > 1 ? days + ' days to go' : days === 1 ? 'Tomorrow!' : days > -3 ? 'It’s happening!' : 'Just married';

  // The same countdown, painted in Portuguese on the tile above the RSVP door
  var tile = document.querySelector('.count-tile');
  function paintTile(num, word) {
    tile.querySelector('.count-num').textContent = num;
    tile.querySelector('.count-word').textContent = word;
    tile.classList.toggle('one-line', !word);
    tile.title = cd.textContent;
  }
  if (days > 1) paintTile(days, 'dias');
  else if (days === 1) paintTile('amanhã', '');
  else if (days > -3) paintTile('hoje!', '');
  else paintTile('casados', '');

  /* ---------- Wedding weekend (1–3 Oct 2027): party mode ----------
     Preview any time by adding ?party to the address. */

  var party = (now >= new Date(2027, 9, 1) && now < new Date(2027, 9, 4)) || /[?&]party(=|&|$)/.test(location.search);
  if (party) {
    document.documentElement.classList.add('party');
    cd.textContent = 'It’s happening!';
    paintTile('hoje!', '');
    picture.appendChild(bunting());
    try {
      if (!sessionStorage.getItem('partyHello')) {
        sessionStorage.setItem('partyHello', '1');
        setTimeout(function () { window.toast && window.toast('Welcome to the party! Eat well, dance lots, love always.', 6000); }, 1200);
      }
    } catch (e) {}
  }

  // Strings of paper flags between the chimneys (picture pixels; the sky is negative y)
  function bunting() {
    var NS = 'http://www.w3.org/2000/svg';
    var svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('class', 'bunting');
    svg.setAttribute('viewBox', '0 -360 1926 1177');
    svg.setAttribute('preserveAspectRatio', 'none');
    svg.setAttribute('aria-hidden', 'true');
    var colours = ['#2f5fb5', '#f2b705', '#e8664a', '#7b8152', '#fff6e0'];
    [[205, 70, 690, 270, 1165, 72], [1173, 72, 1490, 240, 1800, 70]].forEach(function (g, gi) {
      var x0 = g[0], y0 = g[1], cx = g[2], cy = g[3], x1 = g[4], y1 = g[5];
      var line = document.createElementNS(NS, 'path');
      line.setAttribute('class', 'string');
      line.setAttribute('d', 'M' + x0 + ' ' + y0 + 'Q' + cx + ' ' + cy + ' ' + x1 + ' ' + y1);
      svg.appendChild(line);
      var n = Math.round((x1 - x0) / 46);
      for (var i = 1; i < n; i++) {
        var t = i / n, u = 1 - t;
        var x = u * u * x0 + 2 * u * t * cx + t * t * x1;
        var y = u * u * y0 + 2 * u * t * cy + t * t * y1;
        var dx = 2 * u * (cx - x0) + 2 * t * (x1 - cx);
        var dy = 2 * u * (cy - y0) + 2 * t * (y1 - cy);
        var ang = Math.atan2(dy, dx) * 180 / Math.PI;
        var flag = document.createElementNS(NS, 'path');
        flag.setAttribute('d', 'M-15 0L15 0L0 36Z');
        flag.setAttribute('fill', colours[(i + gi * 2) % colours.length]);
        flag.setAttribute('stroke', 'rgba(90,70,50,.25)');
        flag.setAttribute('transform', 'translate(' + x.toFixed(1) + ' ' + y.toFixed(1) + ') rotate(' + ang.toFixed(1) + ')');
        svg.appendChild(flag);
      }
    });
    return svg;
  }

  /* ---------- Small screens: start in the middle of the street ---------- */

  if (scroller.scrollWidth > scroller.clientWidth) {
    scroller.scrollLeft = (scroller.scrollWidth - scroller.clientWidth) * 0.42;
    var hint = document.querySelector('.swipe-hint');
    // listen only after our own initial scroll has settled, so the hint stays until the visitor swipes
    if (hint) setTimeout(function () {
      scroller.addEventListener('scroll', function () { hint.classList.add('gone'); }, { once: true, passive: true });
    }, 400);
  }

  /* ---------- Scroll: village fades out, story map grows in ---------- */

  var story = document.querySelector('.story');
  var frame = story.querySelector('.story-frame');
  var storyUrl = (story.dataset.storymap || '').trim();
  var loaded = false;

  function loadStory() {
    if (loaded || !storyUrl) return;
    loaded = true;
    var f = document.createElement('iframe');
    f.src = storyUrl;
    f.title = 'Our story – ArcGIS StoryMap';
    f.allow = 'fullscreen; geolocation';
    f.allowFullscreen = true;
    frame.innerHTML = '';
    frame.appendChild(f);
  }

  var ticking = false;
  function onScroll() {
    ticking = false;
    var vh = window.innerHeight;
    hero.style.setProperty('--leave', Math.min(1, Math.max(0, scrollY / (hero.offsetHeight * .6))).toFixed(3));
    var ft = frame.getBoundingClientRect().top;
    story.style.setProperty('--p', Math.min(1, Math.max(0, (vh - ft) / (vh * .8))).toFixed(3));
    if (ft < vh * 2) loadStory();
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();
})();
