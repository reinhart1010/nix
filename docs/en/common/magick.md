---
layout: page
title: common/magick (English)
description: "Create, edit, compose, or convert bitmap images."
content_hash: c0ff4b321dcfff9068988054d33d7a1f200432c8
last_modified_at: 2023-10-04
related_topics:
  - title: Nederlands version
    url: /nl/common/magick.html
    icon: bi bi-globe
---
# magick

Create, edit, compose, or convert bitmap images.
ImageMagick version 7+. See `convert` for versions 6 and below.
More information: <https://imagemagick.org/>.

- Convert file type:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.jpg</span>

- Resize an image, making a new copy:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_image.jpg</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100x100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_image.jpg</span>

- Create a GIF using images:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">images.gif</span>

- Create checkerboard pattern:

`magick -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480</span>` pattern:checkerboard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">checkerboard.png</span>

- Convert images to individual PDF pages:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` +adjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">page-%d.pdf</span>
