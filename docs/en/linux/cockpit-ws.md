---
layout: page
title: linux/cockpit-ws (English)
description: "Communicate between the browser application and various configuration tools and services like `cockpit-bridge`."
content_hash: 27f1dca73e1bb0c9f97227d57a65486d9621f9e8
---
# cockpit-ws

Communicate between the browser application and various configuration tools and services like `cockpit-bridge`.
More information: <https://cockpit-project.org/guide/latest/cockpit-ws.8.html>.

- Start with authentication via SSH at `127.0.0.1` with port `22` enabled:

`cockpit-ws --local-ssh`

- Start an HTTP server on a specific port:

`cockpit-ws --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Start and bind to a specific IP address (defaults to `0.0.0.0`):

`cockpit-ws --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>

- Start without TLS:

`cockpit-ws --no-tls`

- Display help:

`cockpit-ws --help`
