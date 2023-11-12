---
layout: page
title: linux/tcpflow (English)
description: "Capture TCP traffic for debugging and analysis."
content_hash: 2352c640af35518a6ce5e34e18de254fb25c825b
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/tcpflow.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/tcpflow.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/tcpflow.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tcpflow

Capture TCP traffic for debugging and analysis.
More information: <https://manned.org/tcpflow>.

- Show all data on the given interface and port:

`tcpflow -c -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>
