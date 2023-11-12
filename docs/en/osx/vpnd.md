---
layout: page
title: osx/vpnd (English)
description: "Listens for incoming VPN connections."
content_hash: 5f0e42a5e3c7cde3fe96c27b22f82a170342211d
last_modified_at: 2023-11-12
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

- Print usage summary and exit:

`vpnd -h`

- Run the daemon for a specific server configuration:

`vpnd -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_id</span>
