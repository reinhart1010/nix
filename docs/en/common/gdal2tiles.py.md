---
layout: page
title: common/gdal2tiles.py (English)
description: "Generate TMS or XYZ tiles for a raster dataset."
content_hash: ff63ee98e4a123d890f6f214e95dc8f737cf0368
last_modified_at: 2024-02-09
tldri18n_status: 2
---
# gdal2tiles.py

Generate TMS or XYZ tiles for a raster dataset.
More information: <https://gdal.org/programs/gdal2tiles.html>.

- Generate TMS tiles for the zoom levels 2 to 5 of a raster dataset:

`gdal2tiles.py --zoom 2-5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>

- Generate XYZ tiles for the zoom levels 2 to 5 of a raster dataset:

`gdal2tiles.py --zoom 2-5 --xyz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>
