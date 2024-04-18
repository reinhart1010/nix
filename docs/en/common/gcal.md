---
layout: page
title: common/gcal (English)
description: "Display calendar."
content_hash: 90fd529f768bc6bda46f0a29a58654b7fd9a60d7
last_modified_at: 2024-04-18
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/gcal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcal

Display calendar.
More information: <https://www.gnu.org/software/gcal>.

- Display calendar for the current month:

`gcal`

- Display calendar for the month of February of the year 2010:

`gcal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2010</span>

- Provide calendar sheet with week numbers:

`gcal --with-week-number`

- Change starting day of week to 1st day of the week (Monday):

`gcal --starting-day=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Display the previous, current and next month surrounding today:

`gcal .`
