---
layout: page
title: common/gdal_contour (English)
description: "Create contour lines and polygons from a digital elevation model."
content_hash: 761e082b8d4a30b142ea89940ab170f77a1f0335
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># gdal_contour

Create contour lines and polygons from a digital elevation model.
More information: <https://gdal.org/programs/gdal_contour.html>.

- Create a vector dataset with contour lines spread over an 100-meter [i]nterval while [a]ttributing the elevation property as "ele":

`gdal_contour -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ele</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100.0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gpkg</span>

- Create a vector dataset with [p]olygons spread over an 100-meter [i]nterval:

`gdal_contour -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100.0</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.tif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gpkg</span>
