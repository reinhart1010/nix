---
layout: page
title: linux/avifenc (English)
description: "AV1 Image File Format (AVIF) encoder."
content_hash: 664dfcc1141cb4f28651dfa5115219e3926b21fd
---
# avifenc

AV1 Image File Format (AVIF) encoder.
More information: <https://aomediacodec.github.io/av1-avif/>.

- Convert a specific PNG image to AVIF:

`avifenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.avif</span>

- Encode with a specific speed, where 0=slowest, 10=fastest, and 6=default:

`avifenc --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.avif</span>
