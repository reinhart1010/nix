---
layout: page
title: osx/sips (English)
description: "Apple Scriptable Image Processing System."
content_hash: 63cf9c57504942cba621fd7ea6a361b5efafe612
related_topics:
  - title: 中文 version
    url: /zh/osx/sips.html
    icon: bi bi-globe
---
# sips

Apple Scriptable Image Processing System.
Raster/Query images and ColorSync ICC Profiles.

- Specify an output directory so that originals do not get modified:

`sips --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/out_dir</span>

- Resample image at specified size, Image aspect ratio may be altered:

`sips -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.ext</span>

- Resample image so height and width aren't greater than specified size (notice the capital Z):

`sips -Z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.ext</span>

- Resample all images in a directory to fit a width of 960px (honoring aspect ratio):

`sips --resampleWidth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">960</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/images</span>

- Convert an image from CMYK to RGB:

`sips --matchTo '/System/Library/ColorSync/Profiles/Generic RGB Profile.icc' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/out_dir</span>

- Remove ColorSync ICC profile from an image:

`sips -d profile --deleteColorManagementProperties `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ext</span>
