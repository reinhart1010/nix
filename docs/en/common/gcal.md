---
layout: page
title: common/gcal (English)
description: "Displays calendar."
content_hash: b9109e6f7fc27bc81f3e0b20c0aac5c5fb5808ec
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/gcal.html
    icon: bi bi-globe
---
# gcal

Displays calendar.
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
