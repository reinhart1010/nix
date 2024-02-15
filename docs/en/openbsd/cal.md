---
layout: page
title: openbsd/cal (English)
description: "Display a calendar with the current day highlighted."
content_hash: 5fb7fe79a1522d564fc823e82a766dcb89184226
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# cal

Display a calendar with the current day highlighted.
More information: <https://man.openbsd.org/cal>.

- Display a calendar for the current month:

`cal`

- Display a calendar for a specific year:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>

- Display a calendar for a specific month and year:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">month</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>

- Display a calendar for the current [y]ear:

`cal -y`

- Display [j]ulian days (starting from one, numbered from January 1):

`cal -j`

- Use [m]onday as week start instead of Sunday:

`cal -m`

- Number [w]eek numbers (incompatible with `-j`):

`cal -w`
