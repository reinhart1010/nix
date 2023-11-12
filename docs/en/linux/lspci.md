---
layout: page
title: linux/lspci (English)
description: "List all PCI devices."
content_hash: f3a0660c9ca9a726122635f9fccdf6932ba5ccf1
last_modified_at: 2023-11-12
related_topics:
  - title: русский version
    url: /ru/linux/lspci.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lspci.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lspci

List all PCI devices.
More information: <https://manned.org/lspci>.

- Show a brief list of devices:

`lspci`

- Display additional info:

`lspci -v`

- Display drivers and modules handling each device:

`lspci -k`

- Show a specific device:

`lspci -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">00:18.3</span>

- Dump info in a readable form:

`lspci -vm`
