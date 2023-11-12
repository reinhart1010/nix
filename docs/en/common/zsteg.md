---
layout: page
title: common/zsteg (English)
description: "Steganography detection tool for PNG and BMP file formats."
content_hash: 0463c29476b12c5d04d6f0cc43292ff4a4a23fb8
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# zsteg

Steganography detection tool for PNG and BMP file formats.
It detects LSB steganography, ZLIB-compressed data, OpenStego, Camouflage and LSB with the Eratosthenes set.
More information: <https://github.com/zed-0xff/zsteg>.

- Detect embedded data in a PNG:

`zsteg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>

- Detect embedded data in a BMP image, using all known methods:

`zsteg --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.bmp</span>

- Detect embedded data in a PNG, iterating pixels vertically and using MSB first:

`zsteg --msb --order yx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>

- Detect embedded data in a BMP image, specifying the bits to consider:

`zsteg --bits `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,2,3|1-3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.bmp</span>

- Detect embedded data in a PNG, extracting only prime pixels and inverting bits:

`zsteg --prime --invert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>

- Detect embedded data in a BMP image, specifying the minimum length of the strings to be found and the find mode:

`zsteg --min-str-len `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --strings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">first|all|longest|none</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.bmp</span>
