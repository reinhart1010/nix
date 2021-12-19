---
layout: page
title: common/arp-scan (English)
description: "Send ARP packets to hosts (specified as IP addresses or hostnames) to scan the local network."
content_hash: 4fe43f9a266f99a8110c63336982a3cd7e499b54
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/arp-scan.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp-scan.html
    icon: bi bi-globe
---
# arp-scan

Send ARP packets to hosts (specified as IP addresses or hostnames) to scan the local network.
More information: <https://github.com/royhills/arp-scan>.

- Scan the current local network:

`arp-scan --localnet`

- Scan an IP network with a custom bitmask:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- Scan an IP network within a custom range:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.0</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.31</span>

- Scan an IP network with a custom net mask:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">255.255.255.0</span>
