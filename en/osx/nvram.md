---
layout: page
title: osx/nvram (English)
description: "Manipulate firmware variables."
content_hash: 62d883ec6c629ba65ec4f5bced2f4b1753334810
---
# nvram

Manipulate firmware variables.
More information: <https://ss64.com/osx/nvram.html>.

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
