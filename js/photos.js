/* Stay page: tap a photo to see the whole of it.
   Markup: <ul class="photos"><li><button class="photo-open"><img …></button></li>…</ul>
   One <dialog> for the page: the photo as large as the screen allows, previous / next,
   arrow keys, swipe, Esc or a tap outside the photo to close. */
(function () {
  'use strict';

  var buttons = Array.prototype.slice.call(document.querySelectorAll('.photo-open'));
  if (!buttons.length || typeof HTMLDialogElement === 'undefined') return;

  var ARROW_L = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>';
  var ARROW_R = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>';
  var CROSS = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';

  var dialog = document.createElement('dialog');
  dialog.className = 'viewer';
  dialog.setAttribute('aria-label', 'Photo');
  dialog.innerHTML =
    '<img class="v-img" alt="">' +
    '<button class="v-btn v-close" type="button" aria-label="Close">' + CROSS + '</button>' +
    '<button class="v-btn v-prev" type="button" aria-label="Previous photo">' + ARROW_L + '</button>' +
    '<button class="v-btn v-next" type="button" aria-label="Next photo">' + ARROW_R + '</button>';
  document.body.appendChild(dialog);

  var img = dialog.querySelector('.v-img');
  var current = 0;

  function show(i) {
    current = (i + buttons.length) % buttons.length;
    var src = buttons[current].querySelector('img');
    img.src = src.currentSrc || src.src;
    img.alt = src.alt;
  }

  buttons.forEach(function (b, i) {
    b.addEventListener('click', function () { show(i); dialog.showModal(); });
  });
  dialog.querySelector('.v-close').addEventListener('click', function () { dialog.close(); });
  dialog.querySelector('.v-prev').addEventListener('click', function () { show(current - 1); });
  dialog.querySelector('.v-next').addEventListener('click', function () { show(current + 1); });

  // a tap on the dark around the photo closes it
  dialog.addEventListener('click', function (e) { if (e.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { e.preventDefault(); show(current - 1); }
    if (e.key === 'ArrowRight') { e.preventDefault(); show(current + 1); }
  });
  dialog.addEventListener('close', function () { buttons[current].focus(); });

  // swipe left / right on touch
  var startX = null;
  img.addEventListener('pointerdown', function (e) { startX = e.clientX; });
  img.addEventListener('pointerup', function (e) {
    if (startX === null) return;
    var dx = e.clientX - startX;
    startX = null;
    if (Math.abs(dx) > 40) show(current + (dx < 0 ? 1 : -1));
  });
})();
