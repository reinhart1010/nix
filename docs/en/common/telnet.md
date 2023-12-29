---
layout: page
title: common/telnet (English)
description: "Connect to a specified port of a host using the telnet protocol."
content_hash: 64c6f215f4053c7b2b3804c5bd7da352d3bc8b03
last_modified_at: 2023-12-29
related_topics:
  - title: 한국어 version
    url: /ko/common/telnet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# telnet

Connect to a specified port of a host using the telnet protocol.
More information: <https://manned.org/telnet>.

- Telnet to the default port of a host:

`telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Telnet to a specific port of a host:

`telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Exit a telnet session:

`quit`

- Emit the default escape character combination for terminating the session:

`<Ctrl> + ]`

- Start `telnet` with "x" as the session termination character:

`telnet -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Telnet to Star Wars animation:

`telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">towel.blinkenlights.nl</span>
