---
layout: page
title: common/calendar (English)
description: "Display upcoming events from a calendar file."
content_hash: d4d87a9c4bb312c4e02ec631ea98129dc5ea6a6f
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/calendar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calendar

Display upcoming events from a calendar file.
More information: <https://www.commandlinux.com/man-page/man1/calendar.1.html>.

- Show events for today and tomorrow (or the weekend on Friday) from the default calendar:

`calendar`

- Look [A]head, showing events for the next 30 days:

`calendar -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>

- Look [B]ack, showing events for the previous 7 days:

`calendar -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- Show events from a custom calendar [f]ile:

`calendar -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
