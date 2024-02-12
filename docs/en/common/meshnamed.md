---
layout: page
title: common/meshnamed (English)
description: "Distributed naming system for IPv6 mesh networks."
content_hash: b4952fe54193db407b69a0aa9e9f420661365a2c
last_modified_at: 2024-02-12
tldri18n_status: 2
---
# meshnamed

Distributed naming system for IPv6 mesh networks.
More information: <https://github.com/zhoreeq/meshname/>.

- Start a local meshname DNS server:

`meshnamed`

- Convert an IPv6 address into a meshname:

`meshnamed -getname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200:6fc8:9220:f400:5cc2:305a:4ac6:967e</span>

- Convert a meshname to an IPv6 address:

`meshnamed -getip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aiag7sesed2aaxgcgbnevruwpy</span>
