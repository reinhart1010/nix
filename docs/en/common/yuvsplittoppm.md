---
layout: page
title: common/yuvsplittoppm (English)
description: "Convert three subsampled Abekas YUV files to one PPM image."
content_hash: b25ff819d17dd7f6f5c354c6d70328c27eccf766
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# yuvsplittoppm

Convert three subsampled Abekas YUV files to one PPM image.
More information: <https://netpbm.sourceforge.net/doc/yuvsplittoppm.html>.

- Read Akebas YUV bytes from three files starting with basename, merge them into a single PPM image and store it in the specified output file:

`yuvsplittoppm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">basename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.ppm</span>
