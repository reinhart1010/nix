---
layout: page
title: common/palmtopnm (English)
description: "Convert a Palm Bitmap file to a PNM image."
content_hash: 5e3ba886563bbd531a72cca7926d8d98744ee3be
last_modified_at: 2023-10-19
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># palmtopnm

Convert a Palm Bitmap file to a PNM image.
More information: <https://netpbm.sourceforge.net/doc/palmtopnm.html>.

- Generate the PNM image as output, for a Palm Bitmap file as input:

`palmtopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>

- Display various information about the input Palm Bitmap file and process:

`palmtopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>

- Generate a histogram of colours in the input Palm Bitmap file to `stderr`:

`palmtopnm -showhist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.palm</span>

- Display version:

`palmtopnm -version`
