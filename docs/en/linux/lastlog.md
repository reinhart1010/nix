---
layout: page
title: linux/lastlog (English)
description: "Show the most recent login of all users or of a user."
content_hash: 9c983c8144aba186043d7f7af510d7c161e2f731
last_modified_at: 2024-02-15
related_topics:
  - title: Deutsch version
    url: /de/linux/lastlog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lastlog

Show the most recent login of all users or of a user.
More information: <https://manned.org/lastlog>.

- Display the most recent login of all users:

`lastlog`

- Display the lastlog record of the specified user:

`lastlog --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display records older than 7 days:

`lastlog --before 7`

- Display records more recent than 3 days:

`lastlog --time 3`
