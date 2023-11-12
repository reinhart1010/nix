---
layout: page
title: common/ogrmerge.py (English)
description: "Merge several vector datasets into a single one."
content_hash: 2100a7f6ea224b38f02598c97f733a8d366138f6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# ogrmerge.py

Merge several vector datasets into a single one.
More information: <https://gdal.org/programs/ogrmerge.html>.

- Create a GeoPackage with a layer for each input Shapefile:

`ogrmerge.py -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GPKG</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gpkg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.shp path/to/input2.shp ...</span>

- Create a virtual datasource (VRT) with a layer for each input GeoJSON:

`ogrmerge.py -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VRT</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.vrt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.geojson path/to/input2.geojson ...</span>

- Concatenate two vector datasets and store source name of dataset in attribute 'source_name':

`ogrmerge.py -single -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GeoJSON</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.geojson</span>` -src_layer_field_name country `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.shp path/to/input2.shp ...</span>
