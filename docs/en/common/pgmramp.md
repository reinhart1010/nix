---
layout: page
title: common/pgmramp (English)
description: "Generate a greyscale map."
content_hash: 134c9f146c24d0fee45206372a43425ccfbb936d
last_modified_at: 2024-02-07
tldri18n_status: 2
---
# pgmramp

Generate a greyscale map.
More information: <https://netpbm.sourceforge.net/doc/pgmramp.html>.

- Generate a left-to-right greyscale map:

`pgmtexture -lr > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>

- Generate a top-to-bottom greyscale map:

`pgmtexture -tb > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>

- Generate a rectangular greyscale map:

`pgmtexture -rectangle > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>

- Generate a elliptical greyscale map:

`pgmtexture -ellipse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>

- Generate a greyscale map from the top-left corner to the bottom-right corner:

`pgmtexture -diagonal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>
