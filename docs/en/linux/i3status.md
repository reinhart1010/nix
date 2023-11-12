---
layout: page
title: linux/i3status (English)
description: "Status line for the i3 window manager."
content_hash: 68dbfab370980574aae63b16416cad9784ee1a46
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# i3status

Status line for the i3 window manager.
This command is usually called from the i3 configuration file.
More information: <https://i3wm.org/i3status/manpage.html>.

- Print the status line to `stdout` periodically, using the default configuration:

`i3status`

- Print the status line to `stdout` periodically, using a specific configuration:

`i3status -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/i3status.conf</span>

- Display the `i3status` version and help:

`i3status -h`
