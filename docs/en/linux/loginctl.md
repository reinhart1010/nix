---
layout: page
title: linux/loginctl (English)
description: "Manage the systemd login manager."
content_hash: 4d6ea8012f5a34455e1b3b96c049ef85dfbc7f62
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># loginctl

Manage the systemd login manager.
More information: <https://www.freedesktop.org/software/systemd/man/loginctl.html>.

- Print all current sessions:

`loginctl list-sessions`

- Print all properties of a specific session:

`loginctl show-session `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_id</span>` --all`

- Print all properties of a specific user:

`loginctl show-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Print a specific property of a user:

`loginctl show-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --property=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">property_name</span>

- Execute a `loginctl` operation on a remote host:

`loginctl list-users -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>
