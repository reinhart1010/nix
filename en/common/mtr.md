---
layout: page
title: common/mtr (English)
description: "Matt's Traceroute: combined traceroute and ping tool."
content_hash: 04f4fdf8c517530b0f574f8255b6942eb086433d
---
# mtr

Matt's Traceroute: combined traceroute and ping tool.
More information: <https://bitwizard.nl/mtr>.

- Traceroute to a host and continuously ping all intermediary hops:

`mtr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Disable IP address and host name mapping:

`mtr -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Generate output after pinging each hop 10 times:

`mtr -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Force IP IPv4 or IPV6:

`mtr -4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Wait for a given time (in seconds) before sending another packet to the same hop:

`mtr -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
