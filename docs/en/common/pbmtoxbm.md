---
layout: page
title: common/pbmtoxbm (English)
description: "Convert a PBM image to a X11 or X10 bitmap."
content_hash: 79b42676ec331c8fec85b126927fe9499a4e6de5
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# pbmtoxbm

Convert a PBM image to a X11 or X10 bitmap.
More information: <https://netpbm.sourceforge.net/doc/pbmtoxbm.html>.

- Convert a PPM image to a X11 XBM file:

`pbmtoxbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xbm</span>

- Explicitly specify whether an X11 or X10 bitmap should be generated:

`pbmtoxbm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11|x10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xbm</span>
