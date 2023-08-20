---
layout: page
title: linux/systemd-notify (English)
description: "Notify the service manager about start-up completion and other daemon status changes."
content_hash: 3be0966410cce5c9d3dfe10d92e698d28c79d514
last_modified_at: 2023-08-20
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemd-notify

Notify the service manager about start-up completion and other daemon status changes.
This command is useless outside systemd service scripts.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-notify.html>.

- Notify systemd that the service has completed its initialization and is fully started. It should be invoked when the service is ready to accept incoming requests:

`systemd-notify --booted`

- Signal to systemd that the service is ready to handle incoming connections or perform its tasks:

`systemd-notify --ready`

- Provide a custom status message to systemd (this information is shown by `systemctl status`):

`systemd-notify --status="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Add custom status message here...</span>`"`
