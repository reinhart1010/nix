---
layout: page
title: linux/diffimg (English)
description: "Calculate intersection between two images."
content_hash: dcdcebb68ee835595f72ac692b990fd351535370
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# diffimg

Calculate intersection between two images.
Note: the supported extensions are `.png`, `.gif`, `.jpg`, `.ps`.
More information: <https://manned.org/diffimg>.

- Calculate the intersection between images and output an image where each pixel is the difference between corresponding pixels in input images:

`diffimg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image1.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image2.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.ext</span>
