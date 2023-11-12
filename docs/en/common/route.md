---
layout: page
title: common/route (English)
description: "Use route cmd to set the route table."
content_hash: 0b147c5fb7ae15f66a572ee638d3d1a0b58d3cd6
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/route.html
    icon: bi bi-globe
tldri18n_status: 2
---
# route

Use route cmd to set the route table.
More information: <https://manned.org/route>.

- Display the information of route table:

`route -n`

- Add route rule:

`sudo route add -net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` netmask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netmask_address</span>` gw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gw_address</span>

- Delete route rule:

`sudo route del -net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` netmask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">netmask_address</span>` dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gw_address</span>
