---
layout: page
title: osx/vpnd (English)
description: "Listens for incoming VPN connections."
content_hash: daaf63895a2ad38da9c99cf90957df861a03b0a8
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/vpnd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vpnd

Listens for incoming VPN connections.
It should not be invoked manually.
More information: <https://keith.github.io/xcode-man-pages/vpnd.8.html>.

- Start the daemon:

`vpnd`

- Run the daemon in the foreground:

`vpnd -x`

- Run the daemon in the foreground and print logs to the terminal:

`vpnd -d`

- Run the daemon in the foreground, print logs to the terminal, and quit after validating arguments:

`vpnd -n`

- Run the daemon for a specific server configuration:

`vpnd -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_id</span>

- Display help:

`vpnd -h`
