---
layout: page
title: linux/avifenc (English)
description: "AV1 Image File Format (AVIF) encoder."
content_hash: 1a1594c79fe60882536c426b5311994d9bcb60af
last_modified_at: 2023-07-30
---
# avifenc

AV1 Image File Format (AVIF) encoder.
More information: <https://aomediacodec.github.io/av1-avif/>.

- Convert a specific PNG image to AVIF:

`avifenc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.avif</span>

- Encode with a specific speed (6=default, 0=slowest and 10=fastest):

`avifenc --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.avif</span>
