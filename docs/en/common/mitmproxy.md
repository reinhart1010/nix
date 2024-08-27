---
layout: page
title: common/mitmproxy (English)
description: "An interactive man-in-the-middle HTTP proxy."
content_hash: c2c64c3b1aae732955d9241fa329c2729e988eba
last_modified_at: 2024-08-27
tldri18n_status: 2
---
# mitmproxy

An interactive man-in-the-middle HTTP proxy.
See also: `mitmweb` and `mitmdump`.
More information: <https://docs.mitmproxy.org/stable/>.

- Start `mitmproxy` with default settings (will listen on port `8080`):

`mitmproxy`

- Start `mitmproxy` bound to a custom address and port:

`mitmproxy --listen-host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--listen-port|-p</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Start `mitmproxy` using a script to process traffic:

`mitmproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--scripts|-s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.py</span>

- Export the logs with SSL/TLS master keys to external programs (wireshark, etc.):

`SSLKEYLOGFILE="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`" mitmproxy`

- Specify mode of operation of the proxy server (`regular` is the default):

`mitmproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--mode|-m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular|transparent|socks5|...</span>

- Set the console layout:

`mitmproxy --console-layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">horizontal|single|vertical</span>
