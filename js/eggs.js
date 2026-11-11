/* Easter eggs, shared by every page.
   - type "sardinha", "sardine" or "sardinka" anywhere → a school of sardines swims by
   - Program page: click the disco ball → light rays + "Dance lots"
   - Weather page: hover / tap the crabs → they walk away and come back
   - Location page: tap the sardine → it swims off and comes back
   - window.toast(text) shows a small message (used by the orange tree on the homepage) */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Toast ---------- */

  var toastEl = null, toastTimer = null;
  window.toast = function (text, ms) {
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.className = 'toast';
      toastEl.setAttribute('role', 'status');
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = text;
    toastEl.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove('show'); }, ms || 4500);
  };

  /* ---------- Sardines ---------- */

  var WORDS = ['sardinha', 'sardine', 'sardinka'];
  var typed = '';
  var swimming = false;

  document.addEventListener('keydown', function (e) {
    var t = e.target;
    if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
    if (e.ctrlKey || e.metaKey || e.altKey || !e.key || e.key.length !== 1) return;
    typed = (typed + e.key.toLowerCase()).slice(-12);
    for (var i = 0; i < WORDS.length; i++) {
      if (typed.slice(-WORDS[i].length) === WORDS[i]) { typed = ''; sardines(); return; }
    }
  });

  function sardines() {
    if (swimming) return;
    swimming = true;
    var school = document.createElement('div');
    school.className = 'school';
    school.setAttribute('aria-hidden', 'true');
    var n = reduceMotion ? 0 : 14;
    var longest = 0;
    for (var i = 0; i < n; i++) {
      var fish = document.createElement('img');
      fish.src = 'assets/art/sardine.webp';
      fish.alt = '';
      var dur = 5 + Math.random() * 3;
      var delay = Math.random() * 1.8;
      longest = Math.max(longest, dur + delay);
      fish.style.top = (8 + Math.random() * 78) + 'vh';
      fish.style.width = (80 + Math.random() * 90) + 'px';
      fish.style.animationDuration = dur + 's, ' + (1.2 + Math.random()) + 's';
      fish.style.animationDelay = delay + 's, ' + delay + 's';
      school.appendChild(fish);
    }
    document.body.appendChild(school);
    window.toast('Sardinhas! The Algarve’s favourite fish.', 4000);
    setTimeout(function () { school.remove(); swimming = false; }, (longest + .5) * 1000);
  }

  /* ---------- Disco ball (Program page) ---------- */

  var ball = document.querySelector('.disco');
  if (ball) {
    var dancing = false;
    function disco() {
      if (dancing) return;
      dancing = true;
      var room = document.createElement('div');
      room.className = 'disco-room';
      room.setAttribute('aria-hidden', 'true');
      var r = ball.getBoundingClientRect();
      room.style.setProperty('--cx', (r.left + r.width / 2) + 'px');
      room.style.setProperty('--cy', (r.top + r.height / 2) + 'px');
      if (!reduceMotion) {
        ['a', 'b'].forEach(function (k) {
          var rays = document.createElement('div');
          rays.className = 'disco-rays ' + k;
          room.appendChild(rays);
        });
      }
      var words = document.createElement('p');
      words.className = 'disco-words';
      words.textContent = 'Dance lots';
      room.appendChild(words);
      document.body.appendChild(room);
      ball.classList.add('spinning');
      requestAnimationFrame(function () { room.classList.add('on'); });
      setTimeout(function () { room.classList.remove('on'); }, 4200);
      setTimeout(function () { room.remove(); ball.classList.remove('spinning'); dancing = false; }, 5000);
    }
    ball.addEventListener('click', disco);
    ball.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); disco(); } });
  }

  /* ---------- Sardine on its tile (Location page) ---------- */

  var fish = document.querySelector('.tile-art .sardine');
  if (fish) {
    function swimAway() {
      if (fish.classList.contains('swimming') || reduceMotion) return;
      fish.classList.add('swimming');
    }
    fish.addEventListener('click', swimAway);
    fish.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); swimAway(); } });
    fish.addEventListener('animationend', function (e) {
      if (e.animationName === 'fish-away') fish.classList.remove('swimming');
    });
  }

  /* ---------- Crabs (Weather page) ---------- */

  var crabs = document.querySelector('.crabs');
  if (crabs) {
    function scuttle() {
      if (crabs.classList.contains('scuttling') || reduceMotion) return;
      crabs.classList.add('scuttling');
    }
    crabs.addEventListener('mouseenter', scuttle);
    crabs.addEventListener('click', scuttle);
    crabs.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); scuttle(); } });
    crabs.addEventListener('animationend', function (e) {
      if (e.animationName === 'crab-walk') crabs.classList.remove('scuttling');
    });
  }
})();
