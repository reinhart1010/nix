---
layout: page
title: common/khal (English)
description: "A text-based calendar and scheduling application for the command-line."
content_hash: a6e4ad6d64e6c0e1dd39cfa3f146328b45d4d6eb
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/khal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# khal

A text-based calendar and scheduling application for the command-line.
More information: <https://lostpackets.de/khal>.

- Start Khal on interactive mode:

`ikhal`

- Print all events scheduled in personal calendar for the next seven days:

`khal list -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7d</span>

- Print all events scheduled not in personal calendar for tomorrow at 10:00:

`khal at -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tomorrow</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10:00</span>

- Print a calendar with a list of events for the next three months:

`khal calendar`

- Add new event to personal calendar:

`khal new -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-09-08</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">18:00</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">18:30</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Dentist appointment</span>`"`
