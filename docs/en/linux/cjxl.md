---
layout: page
title: linux/cjxl (English)
description: "Compress images to JPEG XL."
content_hash: c409fa997ebc2207911ae0d3c5022a302e62ecde
last_modified_at: 2024-08-28
tldri18n_status: 2
---
# cjxl

Compress images to JPEG XL.
Accepted input extensions are PNG, APNG, GIF, JPEG, EXR, PPM, PFM, PAM, PGX, and JXL.
More information: <https://github.com/libjxl/libjxl>.

- Convert an image to JPEG XL:

`cjxl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.jxl</span>

- Set quality to lossless and maximize compression of the resulting image:

`cjxl --distance 0 --effort 9 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.jxl</span>

- Display an extremely detailed help page:

`cjxl --help --verbose --verbose --verbose --verbose`
