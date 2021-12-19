---
layout: page
title: osx/notifyd (English)
description: "Notification server."
content_hash: 2c6296c821c20b6e090bac42b98aa037e043bf44
---
# notifyd

Notification server.
It should not be invoked manually.

- Start the daemon:

`notifyd`

- Log debug messages to the default log file (`/var/log/notifyd.log`):

`notifyd -d`

- Log debug messages to an alternate log file:

`notifyd -d -log_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log</span>
