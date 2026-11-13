/* "Our favourites" map on the Algarve page — ArcGIS Maps SDK for JavaScript.
   Uses js/arcgis-common.js (SDK loading + Marek's "Azulejo Complete" basemap).

   Places live in assets/data/places.geojson. Each feature needs:
     name      – shown on the marker popup and in the list
     category  – "beach", "food", "sight", "kids" or "venue"
     tip       – one or two sentences from you
   Add, remove or move points there (e.g. with geojson.io) and the map follows.

   Overview inset: the same azulejo tiles at small scale, showing where the main map is. */
(function () {
  'use strict';

  var WM = window.WeddingMaps;
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
  if (!WM) return;

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

  // Compact side list: icon + name + category. The details live in the map popup.
  // (Without the map, a click shows the tip inline so nothing is ever lost.)
  function renderList() {
    if (!listEl) return;
    listEl.innerHTML = '';
    places.filter(function (p) { return !activeCat || p.category === activeCat || p.category === 'venue'; })
      .forEach(function (p) {
        var c = CATS[p.category] || CATS.sight;
        var li = document.createElement('li');
        li.className = 'place place-' + p.category;
        li.dataset.name = p.name;
        li.innerHTML =
          '<span class="place-icon"><img src="' + c.icon + '" alt="" width="' + c.w + '" height="' + c.h + '"></span>' +
          '<span class="place-text"><b>' + escapeHtml(p.name) + '</b><span class="place-cat">' + c.label + '</span></span>' +
          '<span class="place-tip">' + escapeHtml(p.tip) + ' <a href="' + directions(p) + '" target="_blank" rel="noopener">Directions&nbsp;&nearr;</a></span>';
        li.tabIndex = 0;
        li.setAttribute('role', 'button');
        function pick(e) {
          if (e && e.target.closest('a')) return;
          setActive(p.name);
          if (api) {
            api.focus(p);
            var r = mapEl.getBoundingClientRect();          // on phones the map sits above the list
            if (r.bottom < 60 || r.top > window.innerHeight - 60) mapEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
          } else {
            li.classList.toggle('show-tip');
          }
        }
        li.addEventListener('click', pick);
        li.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(); } });
        listEl.appendChild(li);
      });
  }

  function setActive(name) {
    if (!listEl) return;
    Array.prototype.forEach.call(listEl.children, function (li) {
      var on = li.dataset.name === name;
      li.setAttribute('aria-current', on ? 'true' : 'false');
      if (on) {                                          // keep the row in view inside the list only
        var top = li.offsetTop - listEl.offsetTop, bottom = top + li.offsetHeight;
        if (top < listEl.scrollTop || bottom > listEl.scrollTop + listEl.clientHeight) {
          listEl.scrollTo({ top: top - 8, behavior: 'smooth' });
        }
      }
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

  WM.whenNear(mapEl, function () {
    WM.load([
      'esri/Map', 'esri/Basemap', 'esri/views/MapView', 'esri/layers/GeoJSONLayer',
      'esri/layers/WebTileLayer', 'esri/layers/VectorTileLayer', 'esri/Graphic', 'esri/core/reactiveUtils'
    ]).then(function (m) { build.apply(null, m); }).catch(function () {
      mapEl.classList.add('failed');
      mapEl.textContent = 'The map could not load right now – the list has everything.';
    });
  });

  function build(Map, Basemap, MapView, GeoJSONLayer, WebTileLayer, VectorTileLayer, Graphic, reactiveUtils) {
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
          var c = CATS[a.category] || CATS.sight;
          var div = document.createElement('div');
          div.className = 'place-popup place-popup-' + a.category;
          div.innerHTML =
            '<span class="pp-cat"><img src="' + c.icon + '" alt="" width="' + c.w + '" height="' + c.h + '">' + c.label + '</span>' +
            '<p>' + escapeHtml(a.tip || '') + '</p>' +
            '<a class="pp-go" href="' + directions({ lat: g.latitude, lon: g.longitude }) + '" target="_blank" rel="noopener">Directions &nearr;</a>';
          return div;
        }
      }
    });

    var map = new Map({ layers: [layer] });
    WM.azulejoBasemap({ Basemap: Basemap, VectorTileLayer: VectorTileLayer, WebTileLayer: WebTileLayer }, map);
    var view = new MapView({
      container: mapEl,
      map: map,
      center: [-7.66, 37.12],
      zoom: 11,
      constraints: { snapToZoom: false, minZoom: 8 },
      popup: {
        dockEnabled: false,
        actions: [],
        visibleElements: { collapseButton: false, featureNavigation: false, actionBar: false }
      },
      ui: { components: ['zoom', 'attribution'] }
    });
    WM.tameScrolling(view, mapEl);                          // don't hijack page scrolling

    layer.when(function () { return layer.queryExtent(); }).then(function (r) {
      if (r.extent) view.goTo(r.extent.expand(1.3), { animate: false });
    });

    /* ---------- Azulejo Atlas overview inset ---------- */
    if (WM.ATLAS) {
      var inset = document.createElement('div');
      inset.className = 'places-overview';
      inset.setAttribute('aria-hidden', 'true');
      mapEl.parentNode.insertBefore(inset, mapEl.nextSibling);
      mapEl.parentNode.classList.add('has-overview');

      var azulejo = new VectorTileLayer({ url: WM.ATLAS, effect: WM.isNight() ? WM.NIGHT_EFFECT : null });
      new MutationObserver(function () { azulejo.effect = WM.isNight() ? WM.NIGHT_EFFECT : null; })
        .observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
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
              view.goTo({ target: f.geometry, zoom: 12.5 }).then(function () {
                view.openPopup({ features: [f], location: f.geometry });
              });
            });
        }
      };
      if (activeCat) api.filter(activeCat);
      // clicking a marker on the map highlights its row in the side list
      reactiveUtils.watch(function () { return view.popup && view.popup.selectedFeature; }, function (f) {
        setActive(f && f.attributes ? f.attributes.name : null);
      });
    });
  }
})();
