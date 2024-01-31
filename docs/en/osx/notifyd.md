---
layout: page
title: osx/notifyd (English)
description: "Notification server."
content_hash: 1446b82765de995dc86513bb087f334f8ee71f2c
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# notifyd

Notification server.
It should not be invoked manually.
More information: <https://keith.github.io/xcode-man-pages/notifyd.8.html>.

- Start the daemon:

`notifyd`

- Log debug messages to the default log file (`/var/log/notifyd.log`):

`notifyd -d`

- Log debug messages to an alternate log file:

`notifyd -d -log_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log_file</span>
