/* "Our favourites" map on the Tavira page — ArcGIS Maps SDK for JavaScript.

   Places live in assets/data/places.geojson. Each feature needs:
     name      – shown on the marker popup and in the list
     category  – "beach", "food", "sight", "kids" or "venue"
     tip       – one or two sentences from you
   Add, remove or move points there (e.g. with geojson.io) and the map follows.

   Basemap: Esri's light / dark grey canvas (follows night mode).
   Overview: Marek's own "Azulejo Atlas" vector tiles (public on ArcGIS Online) in a
   small inset showing where the main map is. The atlas only goes down to ~1:1M
   (Natural Earth data), so it works as an overview rather than the detailed map. */
(function () {
  'use strict';

  var API_KEY = '';
  var AZULEJO = 'https://tiles.arcgis.com/tiles/LlQJoYHf9cwrM7NJ/arcgis/rest/services/Azulejo_Atlas/VectorTileServer';
  var NIGHT_EFFECT = 'brightness(0.62) saturate(0.85)';
  var SDK = 'https://js.arcgis.com/4.31/';                   // pinned SDK version
  var DATA = 'assets/data/places.geojson';

  var CATS = {
    beach: { label: 'Beaches',      icon: 'assets/art/shell.webp',    w: 17, h: 28 },
    food:  { label: 'Eat & drink',  icon: 'assets/art/sardine.webp',  w: 42, h: 15 },
    sight: { label: 'Things to do', icon: 'assets/art/shrimp.webp',   w: 32, h: 24 },
    kids:  { label: 'With kids',    icon: 'assets/art/crabs.webp',    w: 27, h: 28 },
    venue: { label: 'The wedding',  icon: 'assets/logo-mark.png', w: 30, h: 29 }
  };

  var mapEl = document.getElementById('places-map');
  if (!mapEl) return;
  var listEl = document.getElementById('places-list');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.place-chips button'));
  var root = document.documentElement;
  function isNight() { return root.dataset.theme === 'night'; }

  /* ---------- the list under the map works even before / without the SDK ---------- */

  var places = [];
  var api = null;          // filled in once the map is ready: { focus(place), filter(cat) }
  var activeCat = '';

  fetch(DATA).then(function (r) { return r.json(); }).then(function (geo) {
    places = geo.features.map(function (f) {
      var p = f.properties;
      return { name: p.name, category: p.category, tip: p.tip, lon: f.geometry.coordinates[0], lat: f.geometry.coordinates[1] };
    });
    renderList();
  });

  function directions(p) {
    return 'https://www.google.com/maps/dir/?api=1&destination=' + p.lat + ',' + p.lon;
  }

  function renderList() {
    if (!listEl) return;
    listEl.innerHTML = '';
    places.filter(function (p) { return !activeCat || p.category === activeCat || p.category === 'venue'; })
      .forEach(function (p) {
        var c = CATS[p.category] || CATS.sight;
        var li = document.createElement('li');
        li.className = 'place place-' + p.category;
        li.innerHTML =
          '<img src="' + c.icon + '" alt="" width="' + c.w + '" height="' + c.h + '">' +
          '<div><span class="place-cat">' + c.label + '</span>' +
          '<b>' + escapeHtml(p.name) + '</b><p>' + escapeHtml(p.tip) + '</p>' +
          '<a href="' + directions(p) + '" target="_blank" rel="noopener">Directions &nearr;</a></div>';
        li.tabIndex = 0;
        li.addEventListener('click', function (e) {
          if (e.target.closest('a')) return;
          if (api) { api.focus(p); mapEl.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
        });
        li.addEventListener('keydown', function (e) { if (e.key === 'Enter' && api) api.focus(p); });
        listEl.appendChild(li);
      });
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (ch) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch];
    });
  }

  chips.forEach(function (b) {
    b.addEventListener('click', function () {
      activeCat = b.dataset.cat || '';
      chips.forEach(function (c) { c.setAttribute('aria-pressed', String(c === b)); });
      renderList();
      if (api) api.filter(activeCat);
    });
  });

  /* ---------- load the ArcGIS SDK only when the map is about to scroll into view ---------- */

  function loadSdk(cb) {
    var css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = SDK + 'esri/themes/light/main.css';
    document.head.appendChild(css);
    var js = document.createElement('script');
    js.src = SDK + 'init.js';
    js.onload = cb;
    js.onerror = function () { mapEl.classList.add('failed'); mapEl.textContent = 'The map could not load right now – the list below has everything.'; };
    document.head.appendChild(js);
  }

  var started = false;
  function start() {
    if (started) return;
    started = true;
    loadSdk(function () {
      window.require([
        'esri/config', 'esri/Map', 'esri/Basemap', 'esri/views/MapView',
        'esri/layers/GeoJSONLayer', 'esri/layers/WebTileLayer', 'esri/layers/VectorTileLayer',
        'esri/Graphic', 'esri/core/reactiveUtils'
      ], build);
    });
  }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      if (entries.some(function (e) { return e.isIntersecting; })) { io.disconnect(); start(); }
    }, { rootMargin: '400px' });
    io.observe(mapEl);
  } else {
    start();
  }

  function build(esriConfig, Map, Basemap, MapView, GeoJSONLayer, WebTileLayer, VectorTileLayer, Graphic, reactiveUtils) {
    if (API_KEY) esriConfig.apiKey = API_KEY;

    // Esri's light / dark grey canvas (raster tiles, no key needed);
    // with an API key the newer vector styles are used instead.
    var CANVAS = 'https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_';
    function tiles(name) {
      return new WebTileLayer({
        urlTemplate: CANVAS + name + '/MapServer/tile/{level}/{row}/{col}',
        copyright: 'Esri, HERE, Garmin, © OpenStreetMap contributors'
      });
    }
    function canvasBasemap() {
      if (API_KEY) return isNight() ? 'arcgis/dark-gray' : 'arcgis/light-gray';
      var shade = isNight() ? 'Dark_Gray' : 'Light_Gray';
      return new Basemap({ baseLayers: [tiles(shade + '_Base')], referenceLayers: [tiles(shade + '_Reference')] });
    }

    function basemap() { return canvasBasemap(); }

    var renderer = {
      type: 'unique-value',
      field: 'category',
      uniqueValueInfos: Object.keys(CATS).map(function (k) {
        var c = CATS[k];
        return { value: k, label: c.label, symbol: { type: 'picture-marker', url: c.icon, width: c.w + 'px', height: c.h + 'px' } };
      })
    };

    var layer = new GeoJSONLayer({
      url: DATA,
      outFields: ['*'],
      renderer: renderer,
      popupTemplate: {
        title: '{name}',
        content: function (e) {
          var a = e.graphic.attributes, g = e.graphic.geometry;
          var div = document.createElement('div');
          div.className = 'place-popup';
          var p = document.createElement('p');
          p.textContent = a.tip || '';
          var link = document.createElement('a');
          link.href = directions({ lat: g.latitude, lon: g.longitude });
          link.target = '_blank';
          link.rel = 'noopener';
          link.textContent = 'Directions ↗';
          div.appendChild(p);
          div.appendChild(link);
          return div;
        }
      }
    });

    var map = new Map({ basemap: basemap(), layers: [layer] });
    var view = new MapView({
      container: mapEl,
      map: map,
      center: [-7.66, 37.12],
      zoom: 11,
      constraints: { snapToZoom: false, minZoom: 8 },
      popup: { dockEnabled: false, collapseEnabled: false, actions: [] },
      ui: { components: ['zoom', 'attribution'] }
    });
    view.navigation.mouseWheelZoomEnabled = false;          // don't hijack page scrolling
    view.on('click', function () { view.navigation.mouseWheelZoomEnabled = true; });
    mapEl.addEventListener('mouseleave', function () { view.navigation.mouseWheelZoomEnabled = false; });

    layer.when(function () { return layer.queryExtent(); }).then(function (r) {
      if (r.extent) view.goTo(r.extent.expand(1.3), { animate: false });
    });

    var azulejo = null;
    new MutationObserver(function () {
      map.basemap = canvasBasemap();
      if (azulejo) azulejo.effect = isNight() ? NIGHT_EFFECT : null;
    }).observe(root, { attributes: true, attributeFilter: ['data-theme'] });

    /* ---------- Azulejo Atlas overview inset ---------- */
    if (AZULEJO) {
      var inset = document.createElement('div');
      inset.className = 'places-overview';
      inset.setAttribute('aria-hidden', 'true');
      mapEl.parentNode.insertBefore(inset, mapEl.nextSibling);
      mapEl.parentNode.classList.add('has-overview');

      azulejo = new VectorTileLayer({ url: AZULEJO, effect: isNight() ? NIGHT_EFFECT : null });
      var ov = new MapView({
        container: inset,
        map: new Map({ basemap: new Basemap({ baseLayers: [azulejo] }) }),
        center: [-8.1, 39.6],
        scale: 18000000,
        constraints: { snapToZoom: false, rotationEnabled: false },
        ui: { components: [] },
        popupEnabled: false
      });
      // the inset ignores the mouse (pointer-events: none in CSS) – it's a picture, not a second map to pan
      var frame = new Graphic({
        symbol: { type: 'simple-fill', color: [217, 112, 90, 0.18], outline: { color: [196, 84, 60, 1], width: 1.6 } }
      });
      var pin = new Graphic({
        geometry: { type: 'point', longitude: -7.6486, latitude: 37.1273 },
        symbol: { type: 'simple-marker', size: 7, color: [196, 84, 60, 1], outline: { color: [255, 255, 255, 1], width: 1.2 } }
      });
      ov.graphics.addMany([frame, pin]);
      reactiveUtils.watch(function () { return view.stationary && view.extent; }, function (ext) {
        if (!ext) return;
        frame.geometry = ext;
        // big enough frame → show it; tiny frame → the Tavira dot says it all
        frame.visible = ext.width > 30000;
      }, { initial: true });
      azulejo.load().catch(function () { inset.remove(); mapEl.parentNode.classList.remove('has-overview'); });
    }

    view.whenLayerView(layer).then(function (lv) {
      api = {
        filter: function (cat) {
          lv.filter = cat ? { where: "category = '" + cat + "' OR category = 'venue'" } : null;
        },
        focus: function (place) {
          layer.queryFeatures({ where: "name = '" + place.name.replace(/'/g, "''") + "'", returnGeometry: true, outFields: ['*'] })
            .then(function (res) {
              if (!res.features.length) return;
              var f = res.features[0];
              view.goTo({ target: f.geometry, zoom: 13.5 }).then(function () {
                view.openPopup({ features: [f], location: f.geometry });
              });
            });
        }
      };
      if (activeCat) api.filter(activeCat);
    });
  }
})();
