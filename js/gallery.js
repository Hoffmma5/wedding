/* Photo rows (Stay page).
   Markup: <div class="carousel" aria-label="…"><figure class="slide"><img …><figcaption>…</figcaption></figure>…</div>
   - a plain row of photos that starts at the text column and runs off the
     right edge of the screen; swipe / scroll-snap on touch
   - two arrow buttons under the row on desktop, arrow keys when focused
   - click a photo to open it full screen */
(function () {
  'use strict';

  var ICON_PREV = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>';
  var ICON_NEXT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>';

  Array.prototype.forEach.call(document.querySelectorAll('.carousel'), function (root) {
    var slides = Array.prototype.slice.call(root.querySelectorAll('.slide'));
    if (!slides.length) return;

    var track = document.createElement('div');
    track.className = 'c-track';
    track.tabIndex = 0;
    track.setAttribute('role', 'group');
    track.setAttribute('aria-label', (root.getAttribute('aria-label') || 'Photos') + ', ' + slides.length + ' photos');
    slides.forEach(function (s) { track.appendChild(s); });
    root.appendChild(track);

    var prev = button('c-prev', 'Previous photos', ICON_PREV);
    var next = button('c-next', 'Next photos', ICON_NEXT);
    var controls = document.createElement('div');
    controls.className = 'c-controls';
    controls.appendChild(prev);
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

    function page() { return Math.max(200, track.clientWidth * .8); }
    function render() {
      var max = track.scrollWidth - track.clientWidth - 2;
      prev.disabled = track.scrollLeft <= 2;
      next.disabled = track.scrollLeft >= max;
      controls.hidden = max <= 0;
    }
    prev.addEventListener('click', function () { track.scrollBy({ left: -page(), behavior: 'smooth' }); });
    next.addEventListener('click', function () { track.scrollBy({ left: page(), behavior: 'smooth' }); });
    track.addEventListener('scroll', render, { passive: true });
    track.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); next.click(); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); prev.click(); }
    });
    window.addEventListener('resize', render);

    slides.forEach(function (s, i) {
      s.tabIndex = 0;
      s.setAttribute('role', 'button');
      s.setAttribute('aria-label', 'Open photo: ' + (s.querySelector('figcaption') || {}).textContent);
      s.addEventListener('click', function () { openViewer(slides, i); });
      s.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openViewer(slides, i); }
      });
    });
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
