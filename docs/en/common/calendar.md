---
layout: page
title: common/calendar (English)
description: "Display upcoming events from a calendar file."
content_hash: 0dd9676688b01ccc54a56779703109cfad883abc
last_modified_at: 2024-09-25
related_topics:
  - title: فارسی version
    url: /fa/common/calendar.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/calendar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/calendar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calendar

Display upcoming events from a calendar file.
More information: <https://manned.org/calendar>.

- Show events for today and tomorrow (or the weekend on Friday) from the default calendar:

`calendar`

- Look [A]head, showing events for the next 30 days:

`calendar -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- Look [B]ack, showing events for the previous 7 days:

`calendar -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- Show events from a custom calendar [f]ile:

`calendar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
