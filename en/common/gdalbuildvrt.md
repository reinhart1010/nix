---
layout: page
title: common/gdalbuildvrt (English)
description: "Build Virtual Datasets from a list of existing datasets."
content_hash: 8640f181540d2724decad57a54b4c45e201dff4b
---
# gdalbuildvrt

Build Virtual Datasets from a list of existing datasets.
More information: <https://gdal.org/programs/gdalbuildvrt.html>.

- Make a virtual mosaic from all TIFF files contained in a directory:

`gdalbuildvrt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.vrt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory/*.tif</span>

- Make a virtual mosaic from files whose name is specified in a text file:

`gdalbuildvrt -input_file_list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/list.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.vrt</span>

- Make an RGB virtual mosaic from 3 single-band input files:

`gdalbuildvrt -separate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/rgb.vrt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/red.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/green.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/blue.tif</span>

- Make a virtual mosaic with blue background colour (RGB: 0 0 255):

`gdalbuildvrt -hidenodata -vrtnodata "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0 0 255</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.vrt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_directory/*.tif</span>
