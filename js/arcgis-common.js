/* Shared ArcGIS Maps SDK setup for the site's maps (Stay + Algarve pages).

   - loads the SDK (pinned version) once, only when a map is about to scroll into view
   - Marek's "Azulejo Complete" vector tiles as the basemap, dimmed in night mode
   - falls back to Esri's light / dark grey canvas if the azulejo tiles can't load
*/
(function () {
  'use strict';

  var SDK = 'https://js.arcgis.com/4.31/';
  var TILES = 'https://tiles.arcgis.com/tiles/LlQJoYHf9cwrM7NJ/arcgis/rest/services/';
  var root = document.documentElement;
  var sdk = null;

  var WM = window.WeddingMaps = {
    BASEMAP: TILES + 'Azulejo_Complete/VectorTileServer',   // detailed down to street level
    ATLAS: TILES + 'Azulejo_Complete/VectorTileServer',      // the overview inset uses the same tiles at small scale
    NIGHT_EFFECT: 'brightness(0.62) saturate(0.85)',

    isNight: function () { return root.dataset.theme === 'night'; },

    /* Load SDK modules → Promise of an array of modules, in the order asked for. */
    load: function (modules) {
      if (!sdk) {
        sdk = new Promise(function (resolve, reject) {
          var css = document.createElement('link');
          css.rel = 'stylesheet';
          css.href = SDK + 'esri/themes/light/main.css';
          document.head.appendChild(css);
          var js = document.createElement('script');
          js.src = SDK + 'init.js';
          js.onload = resolve;
          js.onerror = reject;
          document.head.appendChild(js);
        });
      }
      return sdk.then(function () {
        return new Promise(function (resolve, reject) {
          window.require(modules, function () { resolve(Array.prototype.slice.call(arguments)); }, reject);
        });
      });
    },

    /* Run fn once el is about to scroll into view. */
    whenNear: function (el, fn) {
      if (!('IntersectionObserver' in window)) { fn(); return; }
      var io = new IntersectionObserver(function (entries) {
        if (entries.some(function (e) { return e.isIntersecting; })) { io.disconnect(); fn(); }
      }, { rootMargin: '400px' });
      io.observe(el);
    },

    /* The azulejo basemap for a Map. m = { Basemap, VectorTileLayer, WebTileLayer }.
       Keeps the night dimming in sync and swaps to the grey canvas if the tiles fail. */
    azulejoBasemap: function (m, map) {
      var tiles = new m.VectorTileLayer({ url: WM.BASEMAP, effect: WM.isNight() ? WM.NIGHT_EFFECT : null });
      var failed = false;
      function canvas() {
        var shade = WM.isNight() ? 'Dark_Gray' : 'Light_Gray';
        function t(name) {
          return new m.WebTileLayer({
            urlTemplate: 'https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_' + name + '/MapServer/tile/{level}/{row}/{col}',
            copyright: 'Esri, HERE, Garmin, © OpenStreetMap contributors'
          });
        }
        return new m.Basemap({ baseLayers: [t(shade + '_Base')], referenceLayers: [t(shade + '_Reference')] });
      }
      map.basemap = new m.Basemap({ baseLayers: [tiles] });
      tiles.load().catch(function () { failed = true; map.basemap = canvas(); });
      new MutationObserver(function () {
        if (failed) map.basemap = canvas();
        else tiles.effect = WM.isNight() ? WM.NIGHT_EFFECT : null;
      }).observe(root, { attributes: true, attributeFilter: ['data-theme'] });
      return tiles;
    },

    /* Page-friendly MapView behaviour: wheel-zoom only after you click the map. */
    tameScrolling: function (view, el) {
      view.navigation.mouseWheelZoomEnabled = false;
      view.on('click', function () { view.navigation.mouseWheelZoomEnabled = true; });
      el.addEventListener('mouseleave', function () { view.navigation.mouseWheelZoomEnabled = false; });
    }
  };
})();
