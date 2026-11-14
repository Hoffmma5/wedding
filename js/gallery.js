/* Photo mosaic (Stay page).
   Markup: <div class="gallery"><div class="mosaic"><button class="ph"><img …></button>…</div>
           <button class="gallery-all">See all N photos</button></div>
   - the first five photos form the mosaic; the rest (.ph.more) are hidden
   - any photo opens the full-screen viewer there; "See all" opens it at the
     first hidden one, and the viewer walks through every photo */
(function () {
  'use strict';

  var ICON_PREV = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>';
  var ICON_NEXT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>';

  Array.prototype.forEach.call(document.querySelectorAll('.gallery'), function (root) {
    var items = Array.prototype.slice.call(root.querySelectorAll('.ph'));
    if (!items.length) return;
    items.forEach(function (b, i) {
      b.addEventListener('click', function () { openViewer(items, i); });
    });
    var all = root.querySelector('.gallery-all');
    if (all) all.addEventListener('click', function () {
      var first = items.findIndex(function (b) { return b.classList.contains('more'); });
      openViewer(items, first < 0 ? 0 : first);
    });
  });

  /* ---------- Full-screen viewer ---------- */

  var viewer, vImg, vCap, vCount, vList = [], vIndex = 0;

  function buildViewer() {
    viewer = document.createElement('dialog');
    viewer.className = 'viewer';
    viewer.setAttribute('aria-label', 'Photos');
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
    vImg.src = img.getAttribute('src');
    vImg.alt = img.alt;
    vCap.textContent = '';
    vCount.textContent = (vIndex + 1) + ' / ' + vList.length;
  }

  function openViewer(list, i) {
    if (!viewer) buildViewer();
    vList = list;
    show(i);
    if (viewer.showModal) viewer.showModal(); else viewer.setAttribute('open', '');
  }
})();
