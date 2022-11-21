---
layout: page
title: osx/icalbuddy (English)
description: "Command-line utility for printing events and tasks from the macOS calendar database."
content_hash: 3d1702906af6231fa9864ead5155dafc14b2b552
last_modified_at: 2022-11-21
related_topics:
  - title: español version
    url: /es/osx/icalbuddy.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/icalbuddy.html
    icon: bi bi-globe
---
# icalBuddy

Command-line utility for printing events and tasks from the macOS calendar database.
More information: <https://hasseg.org/icalBuddy/>.

- Show events later today:

`icalBuddy --includeOnlyEventsFromNowOn eventsToday`

- Show uncompleted tasks:

`icalBuddy uncompletedTasks`

- Show a formatted list separated by calendar for all events today:

`icalBuddy --formatOutput --separateByCalendar eventsToday`

- Show tasks for a specified number of days:

`icalBuddy --includeOnlyEventsFromNowOn "tasksDueBefore:today+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">days</span>`"`

- Show events in a time range:

`icalBuddy eventsFrom:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_date</span>` to:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_date</span>
