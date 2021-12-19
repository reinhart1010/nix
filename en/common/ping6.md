---
layout: page
title: common/ping6 (English)
description: "Send ICMP ECHO_REQUEST packets to network hosts via IPv6 address."
content_hash: 77a7947d8d6285c885ccc2a441502d4a25937549
---
# ping6

Send ICMP ECHO_REQUEST packets to network hosts via IPv6 address.
More information: <https://manned.org/ping6>.

- Ping a host:

`ping6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping a host only a specific number of times:

`ping6 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping a host, specifying the interval in seconds between requests (default is 1 second):

`ping6 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping a host without trying to lookup symbolic names for addresses:

`ping6 -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping a host and ring the bell when a packet is received (if your terminal supports it):

`ping6 -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
