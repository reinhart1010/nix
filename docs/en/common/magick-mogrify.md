---
layout: page
title: common/magick-mogrify (English)
description: "Perform operations on multiple images, such as resizing, cropping, flipping, and adding effects."
content_hash: 9137dc3ce50e8ecb41366d58ea5f5682ba609477
last_modified_at: 2024-11-17
related_topics:
  - title: 한국어 version
    url: /ko/common/magick-mogrify.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-mogrify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick mogrify

Perform operations on multiple images, such as resizing, cropping, flipping, and adding effects.
Changes are applied directly to the original file.
See also: `magick`.
More information: <https://imagemagick.org/script/mogrify.php>.

- Resize all JPEG images in the directory to 50% of their initial size:

`magick mogrify -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>

- Resize all images starting with `DSC` to 800x600:

`magick mogrify -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DSC*</span>

- Convert all PNGs in the directory to JPEG:

`magick mogrify -format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Halve the saturation of all image files in the current directory:

`magick mogrify -modulate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100,50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- Double the brightness of all image files in the current directory:

`magick mogrify -modulate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>

- Reduce file sizes of all GIF images in the current directory by reducing quality:

`magick mogrify -layers 'optimize' -fuzz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7%</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.gif</span>
