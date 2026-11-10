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

  document.querySelector('.tree').addEventListener('click', function () {
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
  var days = Math.ceil((new Date(2027, 9, 1) - new Date()) / 864e5);
  cd.textContent = days > 1 ? days + ' days to go' : days === 1 ? 'Tomorrow!' : days > -3 ? 'It’s happening!' : 'Just married';

  /* ---------- Small screens: start in the middle of the street ---------- */

  if (scroller.scrollWidth > scroller.clientWidth) {
    scroller.scrollLeft = (scroller.scrollWidth - scroller.clientWidth) * 0.42;
    var hint = document.querySelector('.swipe-hint');
    scroller.addEventListener('scroll', function () { hint.classList.add('gone'); }, { once: true, passive: true });
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
