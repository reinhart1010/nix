---
layout: page
title: common/fping (English)
description: "A more powerful ping which can ping multiple hosts."
content_hash: 2dbf1dc153afb9a889523ee86387de293ca36721
last_modified_at: 2024-09-27
tldri18n_status: 2
---
# fping

A more powerful ping which can ping multiple hosts.
More information: <https://fping.org>.

- List alive hosts within a subnet generated from a netmask:

`fping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--alive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--generate</span>` 192.168.1.0/24`

- List alive hosts within a subnet generated from an IP range:

`fping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--alive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--generate</span>` 192.168.1.1 192.168.1.254`

- List unreachable hosts within a subnet generated from a netmask:

`fping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--unreach</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--generate</span>` 192.168.1.0/24`
