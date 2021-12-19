---
layout: page
title: common/arping (English)
description: "Discover and probe hosts in a network using the ARP protocol."
content_hash: d2173820b3f8fb129d3467f77b4e6590d4ba3bb9
related_topics:
  - title: italiano version
    url: /it/common/arping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arping.html
    icon: bi bi-globe
---
# arping

Discover and probe hosts in a network using the ARP protocol.
Useful for MAC address discovery.
More information: <https://github.com/ThomasHabets/arping>.

- Ping a host by ARP request packets:

`arping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Ping a host on a specific interface:

`arping -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Ping a host and stop at the first reply:

`arping -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Ping a host a specific number of times:

`arping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_ip</span>

- Broadcast ARP request packets to update neighbours' ARP caches:

`arping -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_to_broadcast</span>

- Detect duplicated IP addresses in the network by sending ARP requests with a 3 second timeout:

`arping -D -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_to_check</span>
