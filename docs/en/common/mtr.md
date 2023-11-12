---
layout: page
title: common/mtr (English)
description: "Matt's Traceroute: combined traceroute and ping tool."
content_hash: db3161cb45d0688e11059cd0c053f0513f9fd9d3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mtr

Matt's Traceroute: combined traceroute and ping tool.
More information: <https://www.bitwizard.nl/mtr/>.

- Traceroute to a host and continuously ping all intermediary hops:

`mtr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Disable IP address and host name mapping:

`mtr --no-dns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Generate output after pinging each hop 10 times:

`mtr --report-wide `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Force IP IPv4 or IPV6:

`mtr -4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Wait for a given time (in seconds) before sending another packet to the same hop:

`mtr --interval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Display the Autonomous System Number (ASN) for each hop:

`mtr --aslookup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Display both IP address and reverse DNS name:

`mtr --show-ips `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
