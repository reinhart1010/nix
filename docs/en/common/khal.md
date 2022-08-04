---
layout: page
title: common/khal (English)
description: "A text-based calendar and scheduling application for the command-line."
content_hash: c871469b657c96097310d51a0851d5c0a5ca11c0
---
# khal

A text-based calendar and scheduling application for the command-line.
More information: <https://lostpackets.de/khal>.

- Start khal on interactive mode:

`ikhal`

- Print all events scheduled in personal calendar for the next seven days:

`khal list -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7d</span>

- Print all events scheduled not in personal calendar for tomorrow at 10:00:

`khal at -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tomorrow</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10:00</span>

- Print a calendar with a list of events for the next three months:

`khal calendar`

- Add new event to personal calendar:

`khal new -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-09-08</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">18:00</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">18:30</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Dentist appointment</span>`"`
