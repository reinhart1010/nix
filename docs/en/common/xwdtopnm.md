---
layout: page
title: common/xwdtopnm (English)
description: "Convert an X11 or X10 window dump file to PNM."
content_hash: 8374fe508ed8ab5b384f70eea32cb840def40353
last_modified_at: 2023-11-23
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xwdtopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xwdtopnm

Convert an X11 or X10 window dump file to PNM.
More information: <https://netpbm.sourceforge.net/doc/xwdtopnm.html>.

- Convert a XWD image file to PBM:

`xwdtopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.xwd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pnm</span>

- Display information about the conversion process:

`xwdtopnm -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.xwd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pnm</span>

- Display the contents of the X11 header of the input file:

`xwdtopnm -headerdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.xwd</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.pnm</span>
