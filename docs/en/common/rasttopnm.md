---
layout: page
title: common/rasttopnm (English)
description: "Convert a Sun rasterfile to a PNM file."
content_hash: c952048a5807b2977686ea05d1ca3f78fc2ebdea
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# rasttopnm

Convert a Sun rasterfile to a PNM file.
More information: <https://netpbm.sourceforge.net/doc/rasttopnm.html>.

- Convert a RAST image to a PNM file:

`rasttopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.rast</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Use the color map indices in the raster if they are color values:

`rasttopnm -index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.rast</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
