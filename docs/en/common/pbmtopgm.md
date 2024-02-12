---
layout: page
title: common/pbmtopgm (English)
description: "Convert a PBM image to PGM by averaging areas surrounding individual pixels."
content_hash: 700f181098fea7ffd7fc7c4d5fea9d70808b68bc
last_modified_at: 2024-02-12
tldri18n_status: 2
---
# pbmtopgm

Convert a PBM image to PGM by averaging areas surrounding individual pixels.
See also: `pnmconvol`, `pamditherbw`.
More information: <https://netpbm.sourceforge.net/doc/pbmtopgm.html>.

- Convert PBM image to PGM by averaging the `w`x`h`-sized area surrounding each pixel:

`pbmtopgm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">w</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>
