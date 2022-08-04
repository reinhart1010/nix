---
layout: page
title: linux/lastlog (English)
description: "Show the most recent login of all users or of a given user."
content_hash: b4b8496973c1ab67e914c39ef37f50df75fa948a
related_topics:
  - title: Deutsch version
    url: /de/linux/lastlog.html
    icon: bi bi-globe
---
# lastlog

Show the most recent login of all users or of a given user.
More information: <https://manned.org/lastlog>.

- Display the most recent login of all users:

`lastlog`

- Display the lastlog record of the specified user:

`lastlog --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display records older than 7 days:

`lastlog --before `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- Display records more recent than 3 days:

`lastlog -time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
