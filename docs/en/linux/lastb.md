---
layout: page
title: linux/lastb (English)
description: "Show a listing of last logged in users."
content_hash: 551eeed051f2f10bcd02c0087f3719a574aba23c
related_topics:
  - title: Deutsch version
    url: /de/linux/lastb.html
    icon: bi bi-globe
---
# lastb

Show a listing of last logged in users.
More information: <https://manned.org/lastb>.

- Show a list of all last logged in users:

`sudo lastb`

- Show a list of all last logged in users since a given time:

`sudo lastb --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>

- Show a list of all last logged in users until a given time:

`sudo lastb --until `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>

- Show a list of all logged in users at a specific time:

`sudo lastb --present `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- Show a list of all last logged in users and translate the IP into a hostname:

`sudo lastb --dns`
