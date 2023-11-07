---
layout: page
title: common/pamtotga (English)
description: "Convert a Netpbm image to a TrueVision Targa file."
content_hash: 86120fc58090ad1d6aef1242dccce9d3b45986ea
last_modified_at: 2023-11-07
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pamtotga

Convert a Netpbm image to a TrueVision Targa file.
More information: <https://netpbm.sourceforge.net/doc/pamtotga.html>.

- Convert a Netpbm image to a TrueVision Targa file:

`pamtotga `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.tga</span>

- Specify the color map of the output image:

`pamtotga -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmap|cmap16|mono|rgb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.tga</span>

- Display version:

`pamtotga -version`
