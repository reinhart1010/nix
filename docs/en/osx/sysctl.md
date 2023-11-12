---
layout: page
title: osx/sysctl (English)
description: "Access kernel state information."
content_hash: b0b679d489b3529d81e0d583dc0757bafe12cef4
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/osx/sysctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sysctl

Access kernel state information.
More information: <https://ss64.com/osx/sysctl.html>.

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
