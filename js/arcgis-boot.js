/* Loads ArcGIS Maps SDK for JavaScript 5.2 from the CDN as ES modules:
   Calcite Components (used by popups and widgets) + the SDK core.
   Kept to these two so we don't download the AI / charts / coding components.
   js/arcgis-common.js injects this file as <script type="module"> when a map is needed. */
import "https://js.arcgis.com/calcite-components/5.2.1/index.js";
import "https://js.arcgis.com/5.2/core.js";
