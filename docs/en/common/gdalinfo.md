---
layout: page
title: common/gdalinfo (English)
description: "List various information about a GDAL supported raster dataset."
content_hash: cd884420af904fa9b66cdb938a9c0b4032c2cc60
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gdalinfo

List various information about a GDAL supported raster dataset.
More information: <https://gdal.org/programs/gdalinfo.html>.

- List all supported raster formats:

`gdalinfo --formats`

- List information about a specific raster dataset:

`gdalinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>

- List information about a specific raster dataset in JSON format:

`gdalinfo -json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>

- Show histogram values of a specific raster dataset:

`gdalinfo -hist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>

- List information about a Web Map Service (WMS):

`gdalinfo WMS:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://services.meggsimum.de/geoserver/ows</span>

- List information about a specific dataset of a Web Map Service (WMS):

`gdalinfo WMS:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://services.meggsimum.de/geoserver/ows</span>` -sd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>
