---
layout: page
title: osx/notifyd (English)
description: "Notification server."
content_hash: 4ab48b65c0811b93ef40901bcc3044217e25306e
last_modified_at: 2023-02-20
---
# notifyd

Notification server.
It should not be invoked manually.
More information: <https://www.manpagez.com/man/8/notifyd/>.

- Start the daemon:

`notifyd`

- Log debug messages to the default log file (`/var/log/notifyd.log`):

`notifyd -d`

- Log debug messages to an alternate log file:

`notifyd -d -log_file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log_file</span>
