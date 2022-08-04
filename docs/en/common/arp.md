---
layout: page
title: common/arp (English)
description: "Show and manipulate your system's ARP cache."
content_hash: d8d24e04f1ad2f0d010d614c3ce963989f58179f
related_topics:
  - title: italiano version
    url: /it/common/arp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/arp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp.html
    icon: bi bi-globe
---
# arp

Show and manipulate your system's ARP cache.
More information: <https://manned.org/arp>.

- Show the current ARP table:

`arp -a`

- Clear the entire cache:

`sudo arp -a -d`

- Delete a specific entry:

`arp -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>

- Create an entry in the ARP table:

`arp -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_address</span>
