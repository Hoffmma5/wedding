/* "find us" map on the Stay page — ArcGIS Maps SDK for JavaScript.
   Uses js/arcgis-common.js (SDK loading + Marek's "Azulejo Complete" basemap).
   The hotel is marked with the wedding emblem (the orange); Tavira and Faro airport
   are small dots for orientation. */
(function () {
  'use strict';

  var WM = window.WeddingMaps;
  var el = document.getElementById('venue-map');
  if (!el || !WM) return;

  var HOTEL = { lon: -7.75093, lat: 37.15356 };
  var SPOTS = [
    { name: 'Tavira', lon: -7.6486, lat: 37.1273 },
    { name: 'Faro airport', lon: -7.9659, lat: 37.0144 }
  ];
  var INK = [75, 75, 49];          // the logo's olive
  var CLAY = [196, 84, 60];        // terracotta dots

  WM.whenNear(el, function () {
    WM.load([
      'esri/Map', 'esri/Basemap', 'esri/views/MapView', 'esri/Graphic',
      'esri/layers/GraphicsLayer', 'esri/layers/WebTileLayer', 'esri/layers/VectorTileLayer'
    ]).then(function (m) { build.apply(null, m); }).catch(function () {
      el.classList.add('failed');
      el.textContent = 'The map could not load right now – use the Google Maps button below.';
    });
  });

  function build(Map, Basemap, MapView, Graphic, GraphicsLayer, WebTileLayer, VectorTileLayer) {
    var pins = new GraphicsLayer();
    var map = new Map({ layers: [pins] });
    WM.azulejoBasemap({ Basemap: Basemap, VectorTileLayer: VectorTileLayer, WebTileLayer: WebTileLayer }, map);

    function point(p) { return { type: 'point', longitude: p.lon, latitude: p.lat }; }
    function label(p, text, dy, size, color) {
      return new Graphic({
        geometry: point(p),
        symbol: {
          type: 'text', text: text, color: color, yoffset: dy,
          haloColor: [255, 253, 248, 0.95], haloSize: 1.6,
          font: { family: 'Noto Sans', size: size, weight: 'bold' }
        }
      });
    }

    SPOTS.forEach(function (s) {
      pins.add(new Graphic({
        geometry: point(s),
        symbol: { type: 'simple-marker', size: 7, color: CLAY, outline: { color: [255, 255, 255], width: 1.3 } }
      }));
      pins.add(label(s, s.name, -16, 10, CLAY));
    });

    var hotel = new Graphic({
      geometry: point(HOTEL),
      symbol: { type: 'picture-marker', url: 'assets/logo-mark.png', width: '40px', height: '39px' },
      attributes: { name: 'Hotel Rural Quinta do Marco' },
      popupTemplate: {
        title: 'Hotel Rural Quinta do Marco',
        content: '<div class="place-popup"><p>Sítio do Marco, 632A<br>Santa Catarina da Fonte do Bispo<br>8800-164 Tavira</p>' +
          '<a class="pp-go" href="https://www.google.com/maps/dir/?api=1&destination=' + HOTEL.lat + ',' + HOTEL.lon +
          '" target="_blank" rel="noopener">Directions &nearr;</a></div>'
      }
    });
    pins.add(hotel);
    pins.add(label(HOTEL, 'Quinta do Marco', 28, 12, INK));

    var view = new MapView({
      container: el,
      map: map,
      center: [-7.80, 37.09],
      zoom: 10,
      constraints: { snapToZoom: false, minZoom: 7 },
      popup: {
        dockEnabled: false,
        actions: [],
        visibleElements: { collapseButton: false, featureNavigation: false, actionBar: false }
      },
      ui: { components: ['zoom', 'attribution'] }
    });
    WM.tameScrolling(view, el);

    // frame the hotel, Tavira and the airport together
    view.when(function () {
      var all = [HOTEL].concat(SPOTS);
      var xs = all.map(function (p) { return p.lon; }), ys = all.map(function (p) { return p.lat; });
      view.goTo({
        target: {
          type: 'extent', spatialReference: { wkid: 4326 },
          xmin: Math.min.apply(null, xs), xmax: Math.max.apply(null, xs),
          ymin: Math.min.apply(null, ys), ymax: Math.max.apply(null, ys)
        }
      }, { animate: false }).then(function () { view.zoom = Math.max(view.zoom - 0.6, 7); }).catch(function () {});
    });
  }
})();
