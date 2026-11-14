/* Photo mosaics (Stay page).
   Markup: <div class="photos" aria-label="…"><figure class="slide"><img …></figure>…</div>
   CSS lays the photos out as a mosaic (one large, five small); here every
   photo becomes a button that opens the full-screen viewer, which steps
   through the whole set with arrows, arrow keys or a swipe. */
(function () {
  'use strict';

  var ICON_PREV = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>';
  var ICON_NEXT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>';

  Array.prototype.forEach.call(document.querySelectorAll('.photos'), function (root) {
    var slides = Array.prototype.slice.call(root.querySelectorAll('.slide'));
    slides.forEach(function (s, i) {
      var img = s.querySelector('img');
      s.tabIndex = 0;
      s.setAttribute('role', 'button');
      s.setAttribute('aria-label', 'Open photo ' + (i + 1) + ' of ' + slides.length + (img && img.alt ? ': ' + img.alt : ''));
      s.addEventListener('click', function () { openViewer(slides, i); });
      s.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openViewer(slides, i); }
      });
    });
  });

  /* ---------- Full-screen viewer ---------- */

  var viewer, vImg, vCount, vList = [], vIndex = 0;

  function buildViewer() {
    viewer = document.createElement('dialog');
    viewer.className = 'viewer';
    viewer.setAttribute('aria-label', 'Photo');
    viewer.innerHTML =
      '<figure><img alt=""></figure>' +
      '<button type="button" class="c-btn v-close" aria-label="Close"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>' +
      '<button type="button" class="c-btn v-prev" aria-label="Previous photo">' + ICON_PREV + '</button>' +
      '<button type="button" class="c-btn v-next" aria-label="Next photo">' + ICON_NEXT + '</button>' +
      '<span class="v-count"></span>';
    document.body.appendChild(viewer);
    vImg = viewer.querySelector('img');
    vCount = viewer.querySelector('.v-count');
    viewer.querySelector('.v-close').addEventListener('click', function () { viewer.close(); });
    viewer.querySelector('.v-prev').addEventListener('click', function () { show(vIndex - 1); });
    viewer.querySelector('.v-next').addEventListener('click', function () { show(vIndex + 1); });
    viewer.addEventListener('click', function (e) { if (e.target === viewer || e.target.tagName === 'FIGURE') viewer.close(); });
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
    vImg.src = img.currentSrc || img.src;
    vImg.alt = img.alt;
    vCount.textContent = (vIndex + 1) + ' / ' + vList.length;
  }

  function openViewer(list, i) {
    if (!viewer) buildViewer();
    vList = list;
    show(i);
    if (viewer.showModal) viewer.showModal(); else viewer.setAttribute('open', '');
  }
})();
