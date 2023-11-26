---
layout: page
title: common/pamtowinicon (English)
description: "Convert a PAM image to a Windows ICO file."
content_hash: 927bbb2b59aaf549ffe95183c072f9168f0d6748
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# pamtowinicon

Convert a PAM image to a Windows ICO file.
More information: <https://netpbm.sourceforge.net/doc/pamtowinicon.html>.

- Convert a PAM image file to an ICO file:

`pamtowinicon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ico</span>

- Encode images with resolutions smaller than t in the BMP format and all other images in the PNG format:

`pamtowinicon -pngthreshold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ico</span>

- Make all pixels outside the non-opaque area black:

`pamtowinicon -truetransparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ico</span>
