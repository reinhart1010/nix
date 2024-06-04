---
layout: page
title: common/magick-compare (English)
description: "Create a comparison image to visually annotate the difference between two images."
content_hash: e71b6034a24acc459c0fb7ff997fee3a3b8af218
last_modified_at: 2024-06-04
tldri18n_status: 2
---
# magick compare

Create a comparison image to visually annotate the difference between two images.
See also: `magick`.
More information: <https://imagemagick.org/script/compare.php>.

- Compare two images:

`magick compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/diff.png</span>

- Compare two images using the specified metric:

`magick compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/diff.png</span>
