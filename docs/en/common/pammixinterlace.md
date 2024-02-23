---
layout: page
title: common/pammixinterlace (English)
description: "Merge each row in an image with its two neighbours."
content_hash: 92b3f9ce30bfbc3ed6e6db03455b4afc6058c0a0
last_modified_at: 2024-02-23
tldri18n_status: 2
---
# pammixinterlace

Merge each row in an image with its two neighbours.
See also: `pamdeinterlace`.
More information: <https://netpbm.sourceforge.net/doc/pammixinterlace.html>.

- Merge each row in an image with its two neighbours:

`pammixinterlace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Use the specified filtering mechanism:

`pammixinterlace -filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linear|fir|ffmpeg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Turn on adaptive filtering mode, i.e., only modify pixels that are obviously part of a comb pattern:

`pammixinterlace -adaptive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
