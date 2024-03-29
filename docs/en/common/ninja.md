---
layout: page
title: common/ninja (English)
description: "A Build system designed to be fast."
content_hash: 409ef34f9cfa351bf35dc02b068f6cc22172183b
last_modified_at: 2023-12-27
related_topics:
  - title: 中文 version
    url: /zh/common/ninja.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ninja

A Build system designed to be fast.
More information: <https://ninja-build.org/manual.html>.

- Build in the current directory:

`ninja`

- Build in the current directory, executing 4 jobs at a time in parallel:

`ninja -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Build a program in a given directory:

`ninja -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Show targets (e.g. `install` and `uninstall`):

`ninja -t targets`

- Display help:

`ninja -h`
