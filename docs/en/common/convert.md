---
layout: page
title: common/convert (English)
description: "Convert between image formats, scale, join, and create images, and much more."
content_hash: fe62b54fe2b6a03279b100a5d2583cf863fea33e
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/convert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/convert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/convert.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/convert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/convert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# convert

Convert between image formats, scale, join, and create images, and much more.
Part of ImageMagick.
More information: <https://imagemagick.org/script/convert.php>.

- Convert an image from JPEG to PNG:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.png</span>

- Scale an image to 50% of its original size:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.png</span>` -resize 50% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.png</span>

- Scale an image keeping the original aspect ratio to a maximum dimension of 640x480:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_image.png</span>` -resize 640x480 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.png</span>

- Horizontally append images:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png path/to/image2.png ...</span>` +append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.png</span>

- Vertically append images:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png path/to/image2.png ...</span>` -append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_image.png</span>

- Create a GIF from a series of images with 100ms delay between them:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png path/to/image2.png ...</span>` -delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/animation.gif</span>

- Create an image with nothing but a solid red background:

`convert -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` "xc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#ff0000</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>

- Create a favicon from several images of different sizes:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.png path/to/image2.png ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/favicon.ico</span>
