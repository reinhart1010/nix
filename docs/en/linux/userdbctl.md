---
layout: page
title: linux/userdbctl (English)
description: "Inspect users, groups and group memberships on the system."
content_hash: 6266cd17efaf4d763c212c1ebfaaf8b1d394b8f0
last_modified_at: 2023-09-08
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># userdbctl

Inspect users, groups and group memberships on the system.
More information: <https://www.freedesktop.org/software/systemd/man/userdbctl.html>.

- List all known user records:

`userdbctl user`

- Show details of a specific user:

`userdbctl user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- List all known groups:

`userdbctl group`

- Show details of a specific group:

`userdbctl group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groupname</span>

- List all services currently providing user/group definitions to the system:

`userdbctl services`
