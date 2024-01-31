---
layout: page
title: osx/sysctl (English)
description: "Access kernel state information."
content_hash: 3500db5d38ec8c743d5eb38116cc261c471c3d49
last_modified_at: 2024-01-31
related_topics:
  - title: 中文 version
    url: /zh/osx/sysctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sysctl

Access kernel state information.
More information: <https://keith.github.io/xcode-man-pages/sysctl.8.html>.

- Show all available variables and their values:

`sysctl -a`

- Show Apple model identifier:

`sysctl -n hw.model`

- Show CPU model:

`sysctl -n machdep.cpu.brand_string`

- Show available CPU features (MMX, SSE, SSE2, SSE3, AES, etc):

`sysctl -n machdep.cpu.features`

- Set a changeable kernel state variable:

`sysctl -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">section.tunable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
