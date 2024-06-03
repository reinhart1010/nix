---
layout: page
title: common/magick (English)
description: "Create, edit, compose, or convert between image formats."
content_hash: 2e3f8492cda2dedd95191c3bbd3bfad55d1e688e
last_modified_at: 2024-06-03
related_topics:
  - title: Nederlands version
    url: /nl/common/magick.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick

Create, edit, compose, or convert between image formats.
This tool replaces `convert` in ImageMagick 7+. See `magick convert` to use the old tool in versions 7+.
Some subcommands, such as `mogrify` have their own usage documentation.
More information: <https://imagemagick.org>.

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
