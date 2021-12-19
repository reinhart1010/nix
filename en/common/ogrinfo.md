---
layout: page
title: common/ogrinfo (English)
description: "List information about an OGR-supported data source."
content_hash: 84b944240d67b690f206125e0f0ea06f532705b3
---
# ogrinfo

List information about an OGR-supported data source.
More information: <https://gdal.org/programs/ogrinfo.html>.

- List layers of a GeoPackage:

`ogrinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>`.gpkg`

- Get detailed information about a specific layer of a GeoPackage:

`ogrinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>`.gpkg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layer_name</span>

- Only show summary information about a specific layer of a GeoPackage:

`ogrinfo -so `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>`.gpkg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layer_name</span>
