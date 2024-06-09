---
layout: page
title: common/magick-convert (English)
description: "Convert between image formats, scale, join, and create images, and much more."
content_hash: 8f65450d9a08f4396d356a503dfa480e3a6cb249
last_modified_at: 2024-06-09
related_topics:
  - title: Deutsch version
    url: /de/common/magick-convert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/magick-convert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/magick-convert.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/magick-convert.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/magick-convert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/magick-convert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick convert

Convert between image formats, scale, join, and create images, and much more.
Note: this tool (previously `convert`) has been replaced by `magick` in ImageMagick 7+.
More information: <https://imagemagick.org/script/convert.php>.

- Convert an image from JPEG to PNG:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.png</span>

- Scale an image to 50% of its original size:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.png</span>` -resize 50% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.png</span>

- Scale an image keeping the original aspect ratio to a maximum dimension of 640x480:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.png</span>` -resize 640x480 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.png</span>

- Scale an image to have a specified file size:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.png</span>` -define jpeg:extent=512kb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.jpg</span>

- Vertically/horizontally append images:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png path/to/image2.png ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-append|+append</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.png</span>

- Create a GIF from a series of images with 100ms delay between them:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png path/to/image2.png ...</span>` -delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/animation.gif</span>

- Create an image with nothing but a solid red background:

`magick convert -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` "xc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#ff0000</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>

- Create a favicon from several images of different sizes:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png path/to/image2.png ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/favicon.ico</span>
