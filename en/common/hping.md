---
layout: page
title: common/hping (English)
description: "Command-line oriented TCP/IP packet assembler and analyzer."
content_hash: 75ae1e4d5959e23c04c3f81da6440d373c04200d
related_topics:
  - title: français version
    url: /fr/common/hping.html
    icon: bi bi-globe
---
# hping

Command-line oriented TCP/IP packet assembler and analyzer.
Inspired by the `ping` command.
More information: <http://www.hping.org>.

- Ping localhost over TCP:

`hping3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>

- Ping an IP address over TCP on a specific port:

`hping3 -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>

- Ping an IP address over UDP on port 80:

`hping3 --udp -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>

- Scan a set of TCP ports on a specific IP address:

`hping3 --scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,3000,9000</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>

- Perform a charge test on port 80:

`hping3 --flood -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>
