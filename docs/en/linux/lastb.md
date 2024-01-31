---
layout: page
title: linux/lastb (English)
description: "List last logged in users."
content_hash: 062085c2a1047033472fa3aa95675e6d577745eb
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/linux/lastb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lastb

List last logged in users.
More information: <https://manned.org/lastb>.

- List last logged in users:

`sudo lastb`

- List all last logged in users since a given time:

`sudo lastb --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>

- List all last logged in users until a given time:

`sudo lastb --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>

- List all logged in users at a specific time:

`sudo lastb --present `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- List all last logged in users and translate the IP into a hostname:

`sudo lastb --dns`
