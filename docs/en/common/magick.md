---
layout: page
title: common/magick (English)
description: "Create, edit, compose, or convert between image formats."
content_hash: f5cb952d75b2c037d7d5ec56e6d749596cb30e88
last_modified_at: 2024-03-14
related_topics:
  - title: Nederlands version
    url: /nl/common/magick.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick

Create, edit, compose, or convert between image formats.
ImageMagick version 7+. See `convert` for versions 6 and below.
More information: <https://imagemagick.org/>.

- Convert between image formats:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.jpg</span>

- Resize an image, making a new copy:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.jpg</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100x100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.jpg</span>

- Create a GIF out of all JPEG images in the current directory:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/images.gif</span>

- Create a checkerboard pattern:

`magick -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480</span>` pattern:checkerboard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/checkerboard.png</span>

- Create a PDF file out of all JPEG images in the current directory:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -adjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pdf</span>
