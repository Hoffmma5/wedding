/* Shared by every page: theme toggle, mobile menu, nav background on scroll. */
(function () {
  'use strict';
  var root = document.documentElement;
  var nav = document.querySelector('.nav');
  var toggle = document.querySelector('.theme-toggle');
  var menuBtn = document.querySelector('.menu-toggle');
  var links = document.getElementById('nav-links');

  function syncTheme() {
    var night = root.dataset.theme === 'night';
    toggle.setAttribute('aria-pressed', String(night));
    toggle.setAttribute('aria-label', night ? 'Switch to day' : 'Switch to night');
  }
  window.setTheme = function (theme) {
    root.dataset.theme = theme;
    try { localStorage.setItem('theme', theme); } catch (e) {}
    syncTheme();
  };
  toggle.addEventListener('click', function () {
    window.setTheme(root.dataset.theme === 'night' ? 'day' : 'night');
  });
  syncTheme();

  // Mark the current page in the menu
  var here = location.pathname.split('/').pop() || 'index.html';
  Array.prototype.forEach.call(links.querySelectorAll('a'), function (a) {
    if (a.getAttribute('href') === here) a.setAttribute('aria-current', 'page');
  });

  function setMenu(open) {
    links.classList.toggle('open', open);
    menuBtn.setAttribute('aria-expanded', String(open));
  }
  menuBtn.addEventListener('click', function (e) {
    e.stopPropagation();
    setMenu(!links.classList.contains('open'));
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('#nav-links')) setMenu(false);
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });

  // Footer: "Back to the village" fades out here and zooms out on the home page (village.js)
  var back = document.querySelector('.street-view');
  if (back && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    back.addEventListener('click', function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;   // new tab etc.
      e.preventDefault();
      try { sessionStorage.setItem('zoomOut', '1'); } catch (err) {}
      document.body.classList.add('leaving');
      setTimeout(function () { location.href = back.href; }, 420);
    });
    window.addEventListener('pageshow', function () { document.body.classList.remove('leaving'); });
  }

  function onScroll() { nav.classList.toggle('scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
