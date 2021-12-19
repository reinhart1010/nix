---
layout: page
title: common/fping (English)
description: "A more powerful ping which can ping multiple hosts."
content_hash: 5a7e0c40e47151d24c7f811994c64eb46c3a4ef0
---
# fping

A more powerful ping which can ping multiple hosts.
More information: <https://fping.org>.

- List alive hosts within a subnet generated from a netmask:

`fping -a -g 192.168.1.0/24`

- List alive hosts within a subnet generated from an IP range:

`fping -a -g 192.168.1.1 192.168.1.254`

- List unreachable hosts within a subnet generated from a netmask:

`fping -u -g 192.168.1.0/24`
