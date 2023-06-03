---
layout: page
title: common/mitmproxy (English)
description: "An interactive man-in-the-middle HTTP proxy."
content_hash: 9f50388ec03bd51403bdcc575a0512fd470c742c
last_modified_at: 2023-06-03
---
# mitmproxy

An interactive man-in-the-middle HTTP proxy.
See also: `mitmweb`.
More information: <https://docs.mitmproxy.org/stable/concepts-options>.

- Start `mitmproxy` with default settings:

`mitmproxy`

- Start `mitmproxy` bound to a custom address and port:

`mitmproxy --listen-host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` --listen-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Start `mitmproxy` using a script to process traffic:

`mitmproxy --scripts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.py</span>

- Export the logs with SSL/TLS master keys to external programs (wireshark, etc.):

`SSLKEYLOGFILE="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`" mitmproxy`
