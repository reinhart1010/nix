---
layout: page
title: common/ping (English)
description: "Send ICMP ECHO_REQUEST packets to network hosts."
content_hash: 0997527b093d5315a79c314353eb55cebaf7f5db
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ping.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ping.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ping.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ping.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ping.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping

Send ICMP ECHO_REQUEST packets to network hosts.
More information: <https://manned.org/ping>.

- Ping host:

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping a host only a specific number of times:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping host, specifying the interval in seconds between requests (default is 1 second):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping host without trying to lookup symbolic names for addresses:

`ping -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping host and ring the bell when a packet is received (if your terminal supports it):

`ping -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Also display a message if no response was received:

`ping -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping a host with specific number of pings, per-packet response timeout (`-W`), and total time limit (`-w`) of the entire ping run:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
