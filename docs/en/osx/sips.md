---
layout: page
title: osx/sips (English)
description: "Apple Scriptable Image Processing System."
content_hash: 03f55af19e3950ecda546309afb6d299f25af5e9
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/sips.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/sips.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sips

Apple Scriptable Image Processing System.
Raster/Query images and ColorSync ICC Profiles.
More information: <https://keith.github.io/xcode-man-pages/sips.1.html>.

- Specify an output directory so that originals do not get modified:

`sips --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/out_dir</span>

- Resample image at specified size, Image aspect ratio may be altered:

`sips --resampleHeightWidth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_file.ext</span>

- Resample image so height and width aren't greater than specified size (notice the capital Z):

`sips --resampleHeightWidthMax `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_file.ext</span>

- Resample all images in a directory to fit a width of 960px (honoring aspect ratio):

`sips --resampleWidth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">960</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/images</span>

- Convert an image from CMYK to RGB:

`sips --matchTo "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/out_dir</span>

- Remove ColorSync ICC profile from an image:

`sips --deleteProperty profile --deleteColorManagementProperties `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file.ext</span>
