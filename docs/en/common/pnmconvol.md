---
layout: page
title: common/pnmconvol (English)
description: "Convolute a PNM image."
content_hash: 508e198b2155031284ee30536497997410f90644
last_modified_at: 2024-02-07
tldri18n_status: 2
---
# pnmconvol

Convolute a PNM image.
More information: <https://netpbm.sourceforge.net/doc/pnmconvol.html>.

- Convolve a PNM image with the specified convolution matrix:

`pnmconvol -matrix=-1,3,-1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Convolve a PNM image with the convolution matrix in the specified files, one for each layer in the input image:

`pnmconvol -matrixfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/matrix1,path/to/matrix2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Convolve a PNM image with the convolution matrix in the specified PNM file:

`pnmconvol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/matrix.pnm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Normalize the weights in the convolution matrix such that they add up to one:

`pnmconvol -matrix=-1,3,-1 -normalize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
