---
layout: page
title: common/ninja (English)
description: "A Build system designed to be fast."
content_hash: 1f4ced13c92634bde487dae59a62e3c4fbdffb67
related_topics:
  - title: 中文 version
    url: /zh/common/ninja.html
    icon: bi bi-globe
---
# ninja

A Build system designed to be fast.
More information: <https://ninja-build.org/manual.html>.

- Build in the current directory:

`ninja`

- Build a program in a given directory:

`ninja -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Show targets (e.g. `install` and `uninstall`):

`ninja -t targets`

- Show help:

`ninja -h`
