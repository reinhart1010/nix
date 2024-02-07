---
layout: page
title: common/pgmkernel (English)
description: "Generate a convolution kernel to be used with `pnmconvol`."
content_hash: 62d021aac93ec4ce28758b3e388e5e580fae9250
last_modified_at: 2024-02-07
tldri18n_status: 2
---
# pgmkernel

Generate a convolution kernel to be used with `pnmconvol`.
See also: `pnmconvol`.
More information: <https://netpbm.sourceforge.net/doc/pgmkernel.html>.

- Generate a convolution kernel:

`pgmkernel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>

- Generate a quadratic convolution kernel:

`pgmkernel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>

- Specify the weight of the center in the generated kernel:

`pgmkernel -weight `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pgm</span>
