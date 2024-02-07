---
layout: page
title: common/pnmindex (English)
description: "Build a visual index of multiple PNM images."
content_hash: d1cf1a8ad16cb391dcabdf96fb35b9ca7feed7cf
last_modified_at: 2024-02-07
tldri18n_status: 2
---
# pnmindex

Build a visual index of multiple PNM images.
See also: `pamundice`.
More information: <https://netpbm.sourceforge.net/doc/pnmindex.html>.

- Produce an image containing thumbnails of the specified images in a grid:

`pnmindex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pnm path/to/input2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Specify the size of the (quadratic) thumbnails:

`pnmindex -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pnm path/to/input2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Specify the number of thumbnails per row:

`pnmindex -across `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pnm path/to/input2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Specify the maximum number of colors in the output:

`pnmindex -colors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.pnm path/to/input2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
