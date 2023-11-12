---
layout: page
title: osx/ping (English)
description: "Send ICMP ECHO_REQUEST packets to network hosts."
content_hash: 4b8fdb3299601d1b32f0c74e25e306b8bfc288b3
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/ping.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping

Send ICMP ECHO_REQUEST packets to network hosts.
More information: <https://ss64.com/osx/ping.html>.

- Ping the specified host:

`ping "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`"`

- Ping a host a specific number of times:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping `host`, specifying the interval in `seconds` between requests (default is 1 second):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping `host` without trying to lookup symbolic names for addresses:

`ping -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping `host` and ring the bell when a packet is received (if your terminal supports it):

`ping -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping `host` and prints the time a packet was received (this option is an Apple addition):

`ping --apple-time "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`
