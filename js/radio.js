/* The Portuguese guitar by the yellow house's door: plays fado.
   assets/audio/fado.mp3 ("A Casa da Mariquinhas"), loaded only when the
   guitar is first played. Click to play, click again to pause; it fades
   in and out and loops. */
(function () {
  'use strict';

  var radio = document.querySelector('.fado-guitar');
  if (!radio) return;
  var tip = radio.querySelector('.tip');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var audio = null, fade = null, notesTimer = null;
  var VOLUME = .7;

  function floatNote() {
    var note = document.createElement('span');
    note.className = 'radio-note';
    note.textContent = Math.random() < .5 ? '♪' : '♫';
    note.style.setProperty('--drift', (Math.random() * 40 - 20).toFixed(0) + 'px');
    radio.appendChild(note);
    setTimeout(function () { note.remove(); }, 2600);
  }

  function rampTo(target, ms, done) {
    clearInterval(fade);
    var start = audio.volume, steps = Math.max(1, Math.round(ms / 40)), i = 0;
    fade = setInterval(function () {
      i++;
      audio.volume = Math.min(1, Math.max(0, start + (target - start) * i / steps));
      if (i >= steps) { clearInterval(fade); if (done) done(); }
    }, 40);
  }

  function setPlaying(on) {
    radio.classList.toggle('playing', on);
    radio.setAttribute('aria-pressed', String(on));
    tip.textContent = on ? 'Stop the fado' : 'Play some fado';
    clearInterval(notesTimer);
    if (on && !reduceMotion) { floatNote(); notesTimer = setInterval(floatNote, 900); }
  }

  function play() {
    if (!audio) {
      audio = new Audio('assets/audio/fado.mp3');
      audio.loop = true;
      audio.preload = 'auto';
    }
    audio.volume = 0;
    var p = audio.play();
    setPlaying(true);
    if (p && p.catch) p.catch(function () { setPlaying(false); });
    rampTo(VOLUME, 1200);
  }

  function stop() {
    if (!audio || audio.paused) return;
    setPlaying(false);
    rampTo(0, 600, function () { audio.pause(); });
  }

  radio.addEventListener('click', function (e) {
    e.preventDefault();
    if (audio && !audio.paused && radio.classList.contains('playing')) stop(); else play();
  });
  window.addEventListener('pagehide', function () { if (audio) audio.pause(); });
})();
