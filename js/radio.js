/* The radio in the yellow house's window: plays fado.
   An original, slow fado in A minor (fado menor style), synthesised live with
   Web Audio - no audio files, no copyright. The melody is a Portuguese
   guitar (bright, doubled steel strings, a tremolo on long notes); under it
   a classical guitar (viola) plays bass and chords. The strings are plucked
   with the Karplus-Strong algorithm. Click to play, click again to stop. */
(function () {
  'use strict';

  var radio = document.querySelector('.radio');
  if (!radio) return;
  var tip = radio.querySelector('.tip');
  var AC = window.AudioContext || window.webkitAudioContext;
  if (!AC) { radio.remove(); return; }
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var BPM = 72, BEAT = 60 / BPM;
  // melody: [midi note, beats]; 0 = rest. Eight bars, 4/4.
  var MELODY = [
    [69, 1], [72, .5], [71, .5], [69, 1], [64, 1],                // Am
    [69, .5], [71, .5], [72, .5], [74, .5], [76, 2],              // Am
    [77, .5], [76, .5], [74, .5], [72, .5], [71, 2],              // E7
    [68, 1], [71, 1], [74, 1], [72, .5], [71, .5],                // E7
    [69, 1.5], [71, .5], [72, 1], [76, 1],                        // Am
    [79, .5], [77, .5], [76, .5], [73, .5], [74, 2],              // A7 -> Dm
    [77, 1], [76, .5], [74, .5], [72, .5], [71, .5], [68, 1],     // Dm | E7
    [69, 3], [0, 1]                                               // Am
  ];
  // chords, one per half bar: [bass, [voicing]]
  var AM = [45, [57, 60, 64]], E7 = [40, [56, 59, 62]], A7 = [45, [55, 61, 64]], DM = [50, [57, 62, 65]];
  var CHORDS = [AM, AM, AM, AM, E7, E7, E7, E7, AM, AM, A7, DM, DM, E7, AM, AM];
  var BAR = 4 * BEAT, LOOP = 8 * BAR;

  var ctx = null, master = null, timer = null, nextLoop = 0, notesTimer = null;
  var buffers = {};

  function hz(m) { return 440 * Math.pow(2, (m - 69) / 12); }

  // Karplus-Strong: a burst of noise in a delay line that averages itself
  // away - it sounds like a plucked string. bright = steel, else nylon.
  function string(freq, bright) {
    var key = freq.toFixed(2) + (bright ? 'b' : 'n');
    if (buffers[key]) return buffers[key];
    var sr = ctx.sampleRate, n = Math.round(sr / freq), len = Math.round(sr * (bright ? 2.4 : 1.8));
    var buf = ctx.createBuffer(1, len, sr), out = buf.getChannelData(0);
    var ring = new Float32Array(n), prev = 0;
    for (var i = 0; i < n; i++) {
      var r = Math.random() * 2 - 1;
      ring[i] = bright ? r : (prev = prev * .55 + r * .45);   // nylon: a softer, filtered burst
    }
    var decay = bright ? .9975 : .9955, idx = 0;
    for (var j = 0; j < len; j++) {
      var a = ring[idx], b = ring[(idx + 1) % n];
      out[j] = a;
      ring[idx] = (a + b) * .5 * decay;
      idx = (idx + 1) % n;
    }
    return (buffers[key] = buf);
  }

  function pluck(m, when, gain, bright) {
    var f = hz(m);
    // Portuguese guitar strings come in pairs: two plucks, a hair apart in pitch
    var pair = bright ? [f, f * 1.0035] : [f];
    pair.forEach(function (freq, k) {
      var src = ctx.createBufferSource();
      src.buffer = string(freq, bright);
      var g = ctx.createGain();
      g.gain.value = gain / pair.length;
      src.connect(g).connect(master);
      src.start(when + k * .004);
    });
  }

  function scheduleLoop(t0) {
    // the Portuguese guitar
    var t = t0;
    MELODY.forEach(function (n) {
      var m = n[0], d = n[1] * BEAT;
      if (m) {
        pluck(m, t, .55, true);
        if (n[1] >= 1.5) {                      // tremolo on the long notes
          for (var r = BEAT / 4; r < d - .05; r += BEAT / 4) pluck(m, t + r, .28, true);
        }
      }
      t += d;
    });
    // the viola: bass on the beat, the chord on the off-beats
    CHORDS.forEach(function (c, h) {
      var start = t0 + h * 2 * BEAT;
      pluck(c[0], start, .5, false);
      c[1].forEach(function (m, k) { pluck(m, start + BEAT + k * .018, .2, false); });
    });
  }

  function tick() {
    while (nextLoop < ctx.currentTime + 1) {
      scheduleLoop(nextLoop);
      nextLoop += LOOP;
    }
  }

  function floatNote() {
    var note = document.createElement('span');
    note.className = 'radio-note';
    note.textContent = Math.random() < .5 ? '♪' : '♫';
    note.style.setProperty('--drift', (Math.random() * 40 - 20).toFixed(0) + 'px');
    radio.appendChild(note);
    setTimeout(function () { note.remove(); }, 2600);
  }

  function play() {
    ctx = new AC();
    master = ctx.createGain();
    master.gain.value = 0;
    master.gain.linearRampToValueAtTime(.5, ctx.currentTime + 1);
    // a touch of warmth: roll off the very top
    var tone = ctx.createBiquadFilter();
    tone.type = 'lowpass';
    tone.frequency.value = 5200;
    master.connect(tone).connect(ctx.destination);
    nextLoop = ctx.currentTime + .15;
    tick();
    timer = setInterval(tick, 250);
    if (!reduceMotion) { floatNote(); notesTimer = setInterval(floatNote, 900); }
    radio.classList.add('playing');
    radio.setAttribute('aria-pressed', 'true');
    tip.textContent = 'Stop the fado';
  }

  function stop() {
    if (!ctx) return;
    clearInterval(timer);
    clearInterval(notesTimer);
    var c = ctx, m = master;
    m.gain.cancelScheduledValues(c.currentTime);
    m.gain.setValueAtTime(m.gain.value, c.currentTime);
    m.gain.linearRampToValueAtTime(0, c.currentTime + .6);
    setTimeout(function () { c.close(); }, 700);
    ctx = null;
    buffers = {};
    radio.classList.remove('playing');
    radio.setAttribute('aria-pressed', 'false');
    tip.textContent = 'Play some fado';
  }

  radio.addEventListener('click', function (e) {
    e.preventDefault();
    if (ctx) stop(); else play();
  });
  window.addEventListener('pagehide', stop);
})();
