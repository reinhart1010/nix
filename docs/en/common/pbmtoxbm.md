---
layout: page
title: common/pbmtoxbm (English)
description: "Convert a PBM image to a X11 or X10 bitmap."
content_hash: 6b254f7f5d2df98b934ffc726be2984c0cd41e61
last_modified_at: 2024-02-09
related_topics:
  - title: Nederlands version
    url: /nl/common/pbmtoxbm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbmtoxbm

Convert a PBM image to a X11 or X10 bitmap.
More information: <https://netpbm.sourceforge.net/doc/pbmtoxbm.html>.

- Convert a PBM image to a X11 XBM file:

`pbmtoxbm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xbm</span>

- Explicitly specify whether an X11 or X10 bitmap should be generated:

`pbmtoxbm -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x11|x10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.xbm</span>
