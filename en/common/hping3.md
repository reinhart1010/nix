---
layout: page
title: common/hping3 (English)
description: "Advanced ping utility which supports protocols such TCP, UDP, and raw IP."
content_hash: 87617698e6277a5cb940d1a06649a99ee6c39bd8
---
# hping3

Advanced ping utility which supports protocols such TCP, UDP, and raw IP.
Best run with elevated priviledges.
More information: <https://github.com/antirez/hping>.

- Ping a destination with 4 ICMP ping requests:

`hping3 --icmp --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>

- Scan TCP port 80, scanning from the specific local source port 5090:

`hping3 --verbose --syn --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` --baseport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5090</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>

- Traceroute using a TCP scan to a specific destination port:

`hping3 --traceroute --verbose --syn --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>

- Perform a TCP ACK scan to check if a given host is alive:

`hping3 --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --verbose --destport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_or_hostname</span>
