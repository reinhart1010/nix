---
layout: page
title: linux/lastlog (English)
description: "Show the most recent login of all users or of a given user."
content_hash: 4b9db0b78d672d81bd019e4e93a405ecbaf44e2a
last_modified_at: 2023-12-30
related_topics:
  - title: Deutsch version
    url: /de/linux/lastlog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lastlog

Show the most recent login of all users or of a given user.
More information: <https://manned.org/lastlog>.

- Display the most recent login of all users:

`lastlog`

- Display the lastlog record of the specified user:

`lastlog --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display records older than 7 days:

`lastlog --before 7`

- Display records more recent than 3 days:

`lastlog --time 3`
