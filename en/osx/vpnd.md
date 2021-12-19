---
layout: page
title: osx/vpnd (English)
description: "Listens for incoming VPN connections."
content_hash: 06a025210b0ee441ab8a7812fb0fc763ccfb54a1
---
# vpnd

Listens for incoming VPN connections.
It should not be invoked manually.

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
