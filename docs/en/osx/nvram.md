---
layout: page
title: osx/nvram (English)
description: "Manipulate firmware variables."
content_hash: 968ba83d1e4d09e0885a203c384ef57fc422a5a1
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/nvram.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvram

Manipulate firmware variables.
More information: <https://keith.github.io/xcode-man-pages/nvram.8.html>.

- [p]rint all the variables stored in the NVRAM:

`nvram -p`

- [p]rint all the variables stored in the NVRAM using [x]ML format:

`nvram -xp`

- Modify the value of a firmware variable:

`sudo nvram `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>`"`

- [d]elete a firmware variable:

`sudo nvram -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- [c]lear all the firmware variables:

`sudo nvram -c`

- Set a firmware variable from a specific [x]ML [f]ile:

`sudo nvram -xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xml</span>
