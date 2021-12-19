---
layout: page
title: osx/ping (English)
description: "Send ICMP ECHO_REQUEST packets to network hosts."
content_hash: f2a65cb2d6d59812f545fcb315f1775949dbe2b7
related_topics:
  - title: 中文 version
    url: /zh/osx/ping.html
    icon: bi bi-globe
---
# ping

Send ICMP ECHO_REQUEST packets to network hosts.

- Ping the specified host:

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping a host a specific number of times:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping `host`, specifying the interval in `seconds` between requests (default is 1 second):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping `host` without trying to lookup symbolic names for addresses:

`ping -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping `host` and ring the bell when a packet is received (if your terminal supports it):

`ping -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping `host` and prints the time a packet was received (this option is an Apple addition):

`ping --apple-time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
