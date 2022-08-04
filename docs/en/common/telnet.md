---
layout: page
title: common/telnet (English)
description: "Connect to a specified port of a host using the telnet protocol."
content_hash: 0a0bbd1c50f8f16356724a10e528cf1363d3ac0a
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

`Ctrl + ]`

- Start telnet with "x" as the session termination character:

`telnet -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Telnet to Star Wars animation:

`telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">towel.blinkenlights.nl</span>
