---
layout: page
title: osx/route (English)
description: "Manually manipulate the routing tables."
content_hash: 8feee592fe0a2f6bb3c86f0fd6ab76c1faa6d271
related_topics:
  - title: português (Portugal) version
    url: /pt_PT/osx/route.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/route.html
    icon: bi bi-globe
---
# route

Manually manipulate the routing tables.
Necessitates to be root.
More information: <https://www.manpagez.com/man/8/route/>.

- Add a route to a destination through a gateway:

`sudo route add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_ip_address</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gateway_address</span>`"`

- Add a route to a /24 subnet through a gateway:

`sudo route add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subnet_ip_address</span>`/24" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gateway_address</span>`"`

- Run in test mode (does not do anything, just print):

`sudo route -t add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_ip_address</span>`/24" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gateway_address</span>`"`

- Remove all routes:

`sudo route flush`

- Delete a specific route:

`sudo route delete "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination_ip_address</span>`/24"`

- Lookup and display the route for a destination (hostname or IP address):

`sudo route get "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>`"`
