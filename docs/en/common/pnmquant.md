---
layout: page
title: common/pnmquant (English)
description: "Quantize the colors in a PNM image into a smaller set."
content_hash: 1299c69f4cdfb2fc7ca42d3ce82a1a68dc6a4f7d
last_modified_at: 2023-12-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmquant.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmquant

Quantize the colors in a PNM image into a smaller set.
This command is a combination of `pnmcolormap` and `pnmremap` and accepts the union of their options, except `-mapfile`.
More information: <https://netpbm.sourceforge.net/doc/pnmquant.html>.

- Generate an image using only `n_colors` or less colors as close as possible to the input image:

`pnmquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_colors</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
