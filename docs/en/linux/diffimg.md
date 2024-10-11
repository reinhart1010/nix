---
layout: page
title: linux/diffimg (English)
description: "Calculate intersection between two images."
content_hash: dcdcebb68ee835595f72ac692b990fd351535370
last_modified_at: 2024-10-11
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/diffimg.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># diffimg

Calculate intersection between two images.
Note: the supported extensions are `.png`, `.gif`, `.jpg`, `.ps`.
More information: <https://manned.org/diffimg>.

- Calculate the intersection between images and output an image where each pixel is the difference between corresponding pixels in input images:

`diffimg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image1.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image2.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.ext</span>
