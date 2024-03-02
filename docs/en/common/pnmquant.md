---
layout: page
title: common/pnmquant (English)
description: "Quantize the colors in a PNM image into a smaller set."
content_hash: 90c03e1e2bcbea57e4b0c528f688648c7bd02c11
last_modified_at: 2024-03-02
related_topics:
  - title: Nederlands version
    url: /nl/common/pnmquant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnmquant

Quantize the colors in a PNM image into a smaller set.
This command is a combination of `pnmcolormap` and `pnmremap` and accepts the union of their options, except `-mapfile`.
See also: `pnmquantall`.
More information: <https://netpbm.sourceforge.net/doc/pnmquant.html>.

- Generate an image using only `n_colors` or less colors as close as possible to the input image:

`pnmquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
