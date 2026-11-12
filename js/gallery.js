/* Polaroid carousels (Stay page).
   Markup: <div class="carousel" aria-label="…"><figure class="slide"><img …><figcaption>…</figcaption></figure>…</div>
   - a row of polaroids: the centre one faces you, the others curve away like a ring
   - swipe / scroll-snap on touch, arrows + dots + keyboard on desktop
   - click a side photo to bring it to the middle, click the middle one to open it full screen */
(function () {
  'use strict';

  var ICON_PREV = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>';
  var ICON_NEXT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>';
  var TILTS = [-2.2, 1.6, -1.1, 2.4, -1.8, 1.1, -2.6, 1.9, -1.3, 2.1];   // hand-placed polaroid tilt

  Array.prototype.forEach.call(document.querySelectorAll('.carousel'), function (root) {
    var slides = Array.prototype.slice.call(root.querySelectorAll('.slide'));
    if (!slides.length) return;

    var track = document.createElement('div');
    track.className = 'c-track';
    track.tabIndex = 0;
    track.setAttribute('aria-roledescription', 'carousel');
    track.setAttribute('aria-label', root.getAttribute('aria-label') || 'Photos');
    slides.forEach(function (s, i) {
      s.setAttribute('aria-roledescription', 'slide');
      s.setAttribute('aria-label', (i + 1) + ' of ' + slides.length);
      track.appendChild(s);
    });
    root.appendChild(track);

    var prev = button('c-prev', 'Previous photo', ICON_PREV);
    var next = button('c-next', 'Next photo', ICON_NEXT);
    var dots = document.createElement('div');
    dots.className = 'c-dots';
    slides.forEach(function (s, i) {
      var d = document.createElement('button');
      d.type = 'button';
      d.setAttribute('aria-label', 'Show photo ' + (i + 1));
      d.addEventListener('click', function () { go(i); });
      dots.appendChild(d);
    });
    var controls = document.createElement('div');
    controls.className = 'c-controls';
    controls.appendChild(prev);
    controls.appendChild(dots);
    controls.appendChild(next);
    root.appendChild(controls);

    function button(cls, label, icon) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'c-btn ' + cls;
      b.setAttribute('aria-label', label);
      b.innerHTML = icon;
      return b;
    }

    var current = 0;
    function stepWidth() { return slides[1] ? slides[1].offsetLeft - slides[0].offsetLeft : track.clientWidth; }

    // Place every polaroid on the "ring" according to its distance from the centre
    function layout() {
      var step = Math.max(1, stepWidth());
      var pos = track.scrollLeft / step;
      slides.forEach(function (s, i) {
        var d = i - pos;                          // 0 = centre, ±1 = neighbours…
        var a = Math.min(Math.abs(d), 3);
        var tilt = TILTS[i % TILTS.length] * Math.min(1, a + .35);
        s.style.transform =
          'perspective(1400px) translateZ(' + (-a * 170) + 'px) rotateY(' + (Math.max(-3, Math.min(3, d)) * 26) + 'deg) rotate(' + tilt + 'deg)';
        s.style.opacity = String(Math.max(0, 1 - a * .28));
        s.style.zIndex = String(10 - Math.round(a * 3));
        s.classList.toggle('is-current', Math.abs(d) < .5);
      });
    }
    function render() {
      Array.prototype.forEach.call(dots.children, function (d, i) { d.setAttribute('aria-current', i === current ? 'true' : 'false'); });
      prev.disabled = current === 0;
      next.disabled = current === slides.length - 1;
    }
    function go(i) {
      current = Math.max(0, Math.min(slides.length - 1, i));
      render();
      track.scrollTo({ left: current * stepWidth(), behavior: 'smooth' });
    }
    var settle = null;
    track.addEventListener('scroll', function () {
      layout();
      clearTimeout(settle);
      settle = setTimeout(function () {         // follow manual swipes once they come to rest
        current = Math.max(0, Math.min(slides.length - 1, Math.round(track.scrollLeft / Math.max(1, stepWidth()))));
        render();
      }, 90);
    }, { passive: true });
    prev.addEventListener('click', function () { go(current - 1); });
    next.addEventListener('click', function () { go(current + 1); });
    track.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); go(current + 1); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); go(current - 1); }
    });
    window.addEventListener('resize', function () { track.scrollLeft = current * stepWidth(); layout(); });

    slides.forEach(function (s, i) {
      s.addEventListener('click', function () {
        if (i === current) openViewer(slides, i);
        else go(i);
      });
    });
    layout();
    render();
  });

  /* ---------- Full-screen viewer ---------- */

  var viewer, vImg, vCap, vCount, vList = [], vIndex = 0;

  function buildViewer() {
    viewer = document.createElement('dialog');
    viewer.className = 'viewer';
    viewer.innerHTML =
      '<figure><img alt=""><figcaption></figcaption></figure>' +
      '<button type="button" class="c-btn v-close" aria-label="Close"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>' +
      '<button type="button" class="c-btn v-prev" aria-label="Previous photo">' + ICON_PREV + '</button>' +
      '<button type="button" class="c-btn v-next" aria-label="Next photo">' + ICON_NEXT + '</button>' +
      '<span class="v-count"></span>';
    document.body.appendChild(viewer);
    vImg = viewer.querySelector('img');
    vCap = viewer.querySelector('figcaption');
    vCount = viewer.querySelector('.v-count');
    viewer.querySelector('.v-close').addEventListener('click', function () { viewer.close(); });
    viewer.querySelector('.v-prev').addEventListener('click', function () { show(vIndex - 1); });
    viewer.querySelector('.v-next').addEventListener('click', function () { show(vIndex + 1); });
    viewer.addEventListener('click', function (e) { if (e.target === viewer) viewer.close(); });
    viewer.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') show(vIndex + 1);
      if (e.key === 'ArrowLeft') show(vIndex - 1);
    });
    var x0 = null;
    viewer.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    viewer.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 40) show(vIndex + (dx < 0 ? 1 : -1));
      x0 = null;
    });
  }

  function show(i) {
    vIndex = (i + vList.length) % vList.length;
    var img = vList[vIndex].querySelector('img');
    var cap = vList[vIndex].querySelector('figcaption');
    vImg.src = img.currentSrc || img.src;
    vImg.alt = img.alt;
    vCap.textContent = cap ? cap.textContent : '';
    vCount.textContent = (vIndex + 1) + ' / ' + vList.length;
  }

  function openViewer(list, i) {
    if (!viewer) buildViewer();
    vList = list;
    show(i);
    if (viewer.showModal) viewer.showModal(); else viewer.setAttribute('open', '');
  }
})();
