---
layout: page
title: common/trip (English)
description: "A network diagnostic tool."
content_hash: d953c938c5a8746a0da458465c9847cef85dc0d5
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/trip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trip

A network diagnostic tool.
Combines the functionality of `traceroute` and `ping`.
Designed to assist with the analysis of networking issues.
More information: <https://trippy.rs/>.

- Basic usage with default parameters:

`sudo trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Trace without requiring elevated privileges (supported platforms only):

`trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --unprivileged`

- Trace using `IPv6` only:

`sudo trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --ipv6`

- Trace using the `udp` protocol:

`sudo trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp</span>

- Use custom destination port `443` for `tcp` tracing:

`sudo trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` --target-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">443</span>

- Use custom source port `5000` for `udp` tracing:

`sudo trip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp</span>` --source-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>
