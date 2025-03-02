---
layout: page
title: common/proxify (English)
description: "A versatile and portable proxy for capturing, manipulating, and replaying HTTP/HTTPS traffic on the go."
content_hash: df5f6657aa587b4b6ec17486d929bf45ceb64f73
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/proxify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# proxify

A versatile and portable proxy for capturing, manipulating, and replaying HTTP/HTTPS traffic on the go.
See also: `mitmproxy`.
More information: <https://github.com/projectdiscovery/proxify>.

- Start a HTTP proxy (on the loopback network interface `127.0.0.1` and port `8888`):

`proxify`

- Start a HTTP proxy on a custom network interface and port (may require `sudo` for a port number lower than `1024`):

`proxify -http-addr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>`"`

- Specify output format and output file:

`proxify -output-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jsonl|yaml</span>` -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display help:

`proxify -h`
