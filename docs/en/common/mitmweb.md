---
layout: page
title: common/mitmweb (English)
description: "A web-based interactive man-in-the-middle HTTP proxy."
content_hash: e4a4b321c9ad7d74871957a755d8f2a7bbe1889e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mitmweb

A web-based interactive man-in-the-middle HTTP proxy.
See also: `mitmproxy`.
More information: <https://docs.mitmproxy.org/stable/concepts-options>.

- Start `mitmweb` with default settings:

`mitmweb`

- Start `mitmweb` bound to a custom address and port:

`mitmweb --listen-host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` --listen-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Start `mitmweb` using a script to process traffic:

`mitmweb --scripts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.py</span>
