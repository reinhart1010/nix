---
layout: page
title: common/xwdtopnm (English)
description: "Convert an X11 or X10 window dump file to PNM."
content_hash: 8374fe508ed8ab5b384f70eea32cb840def40353
last_modified_at: 2023-11-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xwdtopnm

Convert an X11 or X10 window dump file to PNM.
More information: <https://netpbm.sourceforge.net/doc/xwdtopnm.html>.

- Convert a XWD image file to PBM:

`xwdtopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.xwd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pnm</span>

- Display information about the conversion process:

`xwdtopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.xwd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pnm</span>

- Display the contents of the X11 header of the input file:

`xwdtopnm -headerdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.xwd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pnm</span>
