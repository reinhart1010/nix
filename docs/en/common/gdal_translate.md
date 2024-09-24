---
layout: page
title: common/gdal_translate (English)
description: "Convert raster data between different formats."
content_hash: f1ce5d65c5d3f3503184704780c15306c998a72d
last_modified_at: 2024-09-24
tldri18n_status: 2
---
# gdal_translate

Convert raster data between different formats.
More information: <https://gdal.org/programs/gdal_translate.html>.

- Convert a raster dataset to JPEG format:

`gdal_translate -of `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">JPEG</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.jpeg</span>

- Assign a projection to a raster dataset:

`gdal_translate -a_srs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EPSG:4326</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.tif</span>

- Reduce the size of a raster dataset to a specific fraction:

`gdal_translate -outsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.tif</span>

- Convert a GeoTiff to a Cloud Optimized GeoTiff:

`gdal_translate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.tif</span>` -of COG -co COMPRESS=LZW`
