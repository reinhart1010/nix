---
layout: page
title: common/ogrinfo (English)
description: "List information about an OGR-supported data source."
content_hash: 9aa8330f741819c34edc4b8a81a02ea1ea7b78a4
---
# ogrinfo

List information about an OGR-supported data source.
More information: <https://gdal.org/programs/ogrinfo.html>.

- List supported formats:

`ogrinfo --formats`

- List layers of a data source:

`ogrinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gpkg</span>

- Get detailed information about a specific layer of a data source:

`ogrinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layer_name</span>

- Only show summary information about a specific layer of a data source:

`ogrinfo -so `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layer_name</span>
