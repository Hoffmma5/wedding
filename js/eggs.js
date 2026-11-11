/* Easter eggs, shared by every page.
   - type "sardinha", "sardine" or "sardinka" anywhere → a school of sardines swims by
   - Program page: click the disco ball → disco lights, "Dance lots" and a short techno loop
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

  /* ---------- Disco ball (Program page): lights + a little house beat ---------- */

  // An original techno loop, synthesised live with Web Audio
  // (no audio files, no copyright). Returns a function that stops it.
  function partyMusic(bars, bpm) {
    var AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return function () {};
    var ctx = new AC();
    var beat = 60 / bpm, step = beat / 4, t0 = ctx.currentTime + .08, end = t0 + bars * 4 * beat;

    var master = ctx.createGain();
    master.gain.setValueAtTime(.0001, ctx.currentTime);
    master.gain.exponentialRampToValueAtTime(.6, t0 + .25);
    master.gain.setValueAtTime(.6, end - .9);
    master.gain.exponentialRampToValueAtTime(.0001, end);
    var comp = ctx.createDynamicsCompressor();
    comp.threshold.value = -18; comp.ratio.value = 6;
    master.connect(comp);
    comp.connect(ctx.destination);

    var noise = ctx.createBuffer(1, ctx.sampleRate, ctx.sampleRate);
    var data = noise.getChannelData(0);
    for (var i = 0; i < data.length; i++) data[i] = Math.random() * 2 - 1;

    // a touch of saturation for the kick and the acid line
    var drive = ctx.createWaveShaper();
    var curve = new Float32Array(1024);
    for (i = 0; i < 1024; i++) { var x = i / 512 - 1; curve[i] = Math.tanh(2.6 * x); }
    drive.curve = curve;
    drive.connect(master);

    function env(node, t, peak, decay, out) {
      var g = ctx.createGain();
      g.gain.setValueAtTime(peak, t);
      g.gain.exponentialRampToValueAtTime(.0001, t + decay);
      node.connect(g);
      g.connect(out || master);
      return g;
    }
    function kick(t) {                                  // deep, punchy, slightly driven
      var o = ctx.createOscillator();
      o.frequency.setValueAtTime(165, t);
      o.frequency.exponentialRampToValueAtTime(48, t + .09);
      o.frequency.exponentialRampToValueAtTime(40, t + .4);
      env(o, t, 1.1, .42, drive);
      o.start(t); o.stop(t + .45);
    }
    function hiss(t, type, freq, peak, decay, q) {
      var src = ctx.createBufferSource();
      src.buffer = noise;
      var f = ctx.createBiquadFilter();
      f.type = type; f.frequency.value = freq; if (q) f.Q.value = q;
      src.connect(f);
      env(f, t, peak, decay);
      src.start(t, Math.random() * .5); src.stop(t + decay + .02);
    }
    function acid(t, freq, cutoff, accent) {           // squelchy 303-style line
      var o = ctx.createOscillator();
      o.type = 'sawtooth'; o.frequency.value = freq;
      var f = ctx.createBiquadFilter();
      f.type = 'lowpass'; f.Q.value = 14;
      f.frequency.setValueAtTime(cutoff * (accent ? 1.8 : 1), t);
      f.frequency.exponentialRampToValueAtTime(180, t + step * .9);
      o.connect(f);
      env(f, t, accent ? .26 : .17, step * .95, drive);
      o.start(t); o.stop(t + step);
    }

    // A minor acid riff, 16 sixteenth-notes per bar (0 = rest)
    var A1 = 55, C2 = 65.41, D2 = 73.42, E2 = 82.41, G2 = 98, A2 = 110;
    var riff = [A1, A1, A2, A1, 0, A1, C2, A1, A1, E2, A1, A2, D2, A1, G2, E2];
    var accents = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0];

    for (var bar = 0; bar < bars; bar++) {
      var cutoff = 420 + bar / Math.max(1, bars - 1) * 2200;   // filter opens up as it builds
      for (var n = 0; n < 16; n++) {
        var t = t0 + (bar * 16 + n) * step;
        if (n % 4 === 0) kick(t);
        if (n % 4 === 2) hiss(t, 'highpass', 6500, .3, .14);          // open hat on the off-beat
        else hiss(t, 'highpass', 9500, n % 2 ? .1 : .06, .03);        // closed 16th hats
        if (n === 4 || n === 12) hiss(t, 'bandpass', 1300, .6, .18, 1.2);   // clap on 2 and 4
        if (riff[n]) acid(t, riff[n] * (bar % 2 && n === 14 ? 2 : 1), cutoff, accents[n]);
      }
    }
    var timer = setTimeout(function () { ctx.close(); }, (end - ctx.currentTime + .3) * 1000);
    return function stop() {
      clearTimeout(timer);
      try {
        master.gain.cancelScheduledValues(ctx.currentTime);
        master.gain.setTargetAtTime(.0001, ctx.currentTime, .08);
        setTimeout(function () { ctx.close(); }, 400);
      } catch (e) {}
    };
  }

  var ball = document.querySelector('.disco');
  if (ball) {
    var dancing = false;
    var BPM = 132, BARS = 4, LENGTH = BARS * 4 * 60 / BPM * 1000;   // ≈ 7.3 s

    function disco() {
      if (dancing) return;
      dancing = true;
      var stopMusic = partyMusic(BARS, BPM);

      var room = document.createElement('div');
      room.className = 'disco-room beat';
      room.style.setProperty('--beat', (60 / BPM) + 's');
      var r = ball.getBoundingClientRect();
      room.style.setProperty('--cx', (r.left + r.width / 2) + 'px');
      room.style.setProperty('--cy', (r.top + r.height / 2) + 'px');

      var colours = ['#ffffff', '#cfe0ff', '#ffd6e7', '#fff1b8', '#d7fff4'];
      for (var i = 0; i < (reduceMotion ? 0 : 60); i++) {
        var s = document.createElement('i');
        s.setAttribute('aria-hidden', 'true');
        s.style.left = (Math.random() * 100) + 'vw';
        s.style.top = (Math.random() * 100) + 'vh';
        s.style.background = s.style.color = colours[i % colours.length];
        s.style.animationDelay = (-Math.random() * 2) + 's, ' + (-(i % 4) * 15 / BPM) + 's';
        room.appendChild(s);
      }
      var words = document.createElement('p');
      words.className = 'disco-words';
      words.setAttribute('aria-hidden', 'true');
      words.textContent = 'Dance lots';
      room.appendChild(words);

      var mute = document.createElement('button');
      mute.type = 'button';
      mute.className = 'disco-mute';
      mute.textContent = 'Stop the party';
      room.appendChild(mute);

      document.body.appendChild(room);
      ball.classList.add('spinning');
      requestAnimationFrame(function () { room.classList.add('on'); });

      var t1 = setTimeout(finish, LENGTH - 600);
      function finish() {
        clearTimeout(t1);
        stopMusic();
        document.removeEventListener('keydown', onKey);
        room.classList.remove('on');
        setTimeout(function () { room.remove(); ball.classList.remove('spinning'); dancing = false; }, 700);
      }
      function onKey(e) { if (e.key === 'Escape') finish(); }
      mute.addEventListener('click', finish);
      document.addEventListener('keydown', onKey);
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
