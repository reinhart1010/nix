---
layout: page
title: common/pnmpsnr (English)
description: "Compute the difference between two images."
content_hash: b9068657dfee6f734f9bbb7357e75288a8b3c384
last_modified_at: 2024-02-02
tldri18n_status: 2
---
# pnmpsnr

Compute the difference between two images.
More information: <https://netpbm.sourceforge.net/doc/pnmpsnr.html>.

- Compute the difference, i.e. the peak signal-to-noise ratio (PSNR) between two images:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.pnm</span>

- Compare the color components rather than the luminance and chrominance components of the images:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.pnm</span>` -rgb`

- Run in comparison mode, i.e. only output `nomatch` or `match` depending on whether the computing PSNR exceeds `n` or not:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.pnm</span>` -target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Run in comparison mode and compare the individual image components, i.e. Y, Cb, and Cr, to the corresponding thresholds:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.pnm</span>` -target1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">threshold_Y</span>` -target2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">threshold_Cb</span>` -target3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">threshold_Cr</span>

- Run in comparison mode and compare the individual image components, i.e. red, green, and blue to the corresponding thresholds:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.pnm</span>` -rgb -target1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">threshold_red</span>` -target2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">threshold_green</span>` -target3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">threshold_blue</span>

- Produce machine-readable output:

`pnmpsnr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.pnm</span>` -machine`
