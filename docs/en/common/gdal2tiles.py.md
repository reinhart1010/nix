---
layout: page
title: common/gdal2tiles.py (English)
description: "Generate TMS or XYZ tiles for a raster dataset."
content_hash: 3729fb7a026e9a1fc529d1f5ac7fc6b35ce6da9b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gdal2tiles.py

Generate TMS or XYZ tiles for a raster dataset.
More information: <https://gdal.org/programs/gdal2tiles.html>.

- Generate TMS tiles for the zoom levels 2-5 of a raster dataset:

`gdal2tiles.py --zoom=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2-5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>

- Generate XYZ tiles for the zoom levels 2-5 of a raster dataset:

`gdal2tiles.py --zoom=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2-5</span>` --xyz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>
