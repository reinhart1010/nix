---
layout: page
title: linux/smem (English)
description: "Print memory usage for programs."
content_hash: 572e9443b7150db2182bcc5ba98fe8cd67c38c4b
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># smem

Print memory usage for programs.
More information: <https://manned.org/smem>.

- Print memory usage for current processes:

`smem`

- Print memory usage for current processes for a every user on a system:

`smem --users`

- Print memory usage for current processes for a specified user:

`smem --userfilter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Print system memory information:

`smem --system`
