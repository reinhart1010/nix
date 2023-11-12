---
layout: page
title: common/ogrinfo (English)
description: "List information about an OGR-supported data source."
content_hash: fd7caa607bf1681a6d8e6a17d97c59b7e1f26f4f
last_modified_at: 2023-11-12
tldri18n_status: 2
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

- Show summary information about a specific layer of a data source:

`ogrinfo -so `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layer_name</span>

- Show summary of all layers of the data source:

`ogrinfo -so -al `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gpkg</span>

- Show detailed information of features matching a condition:

`ogrinfo -where '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute_name > 42</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layer_name</span>

- Update a layer in the data source with SQL:

`ogrinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.geojson</span>` -dialect SQLite -sql "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UPDATE input SET attribute_name = 'foo'</span>`"`
