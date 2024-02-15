---
layout: page
title: freebsd/cal (English)
description: "Display a calendar with the current day highlighted."
content_hash: 32fd171661ba2bd120ef5e664e3a3ae92b4e4b10
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# cal

Display a calendar with the current day highlighted.
More information: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Display a calendar for the current month:

`cal`

- Display a calendar for a specific year:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>

- Display a calendar for a specific month and year:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">month</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>

- Display the whole calendar for the current year:

`cal -y`

- Don't [h]ighlight today and display [3] months spanning the date:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">month</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>

- Display the 2 months [B]efore and 3 [A]fter a specific [m]onth of the current year:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">month</span>

- Display [j]ulian days (starting from one, numbered from January 1):

`cal -j`
