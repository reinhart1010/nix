---
layout: page
title: netbsd/cal (English)
description: "Display a calendar."
content_hash: e9738d6042c142687e86416a74cc0649c031e72f
last_modified_at: 2024-09-19
related_topics:
  - title: 한국어 version
    url: /ko/netbsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

Display a calendar.
More information: <https://man.netbsd.org/cal.1>.

- Display a calendar for the current month:

`cal`

- Display a calendar for a specific year:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>

- Display a calendar for a specific month and year:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">month</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>

- Display the whole calendar for the current year using [j]ulian days (one-based, numbered from January 1):

`cal -y -j`

- [h]ighlight today and display [3] months spanning the date:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">month</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>

- Display the 2 months [B]efore and 3 [A]fter a specific [m]onth of the current year:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">month</span>

- Display a specific number of months before and after ([C]ontext) the specified month:

`cal -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">months</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">month</span>

- Specify the starting [d]ay of the week (0: Sunday, 1: Monday, ..., 6: Saturday):

`cal -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..6</span>
