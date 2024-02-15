---
layout: page
title: netbsd/cal (English)
description: "Display a calendar."
content_hash: 6f3776d89fb72068ad8d67e26cf4a001d6775899
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# cal

Display a calendar.
More information: <https://man.freebsd.org/cgi/man.cgi?cal>.

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
