---
layout: page
title: osx/vpnd (English)
description: "Listens for incoming VPN connections."
content_hash: 482601de0ac20c0ea37db9e69940b73753540bda
last_modified_at: 2024-01-30
related_topics:
  - title: español version
    url: /es/osx/vpnd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vpnd

Listens for incoming VPN connections.
It should not be invoked manually.
More information: <https://www.unix.com/man-page/osx/8/vpnd/>.

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
