---
layout: page
title: osx/icalbuddy (English)
description: "Command-line utility for printing events and tasks from the macOS calendar database."
content_hash: 9788bbf9a448980dc08beb49433df2a00d190690
---
# icalBuddy

Command-line utility for printing events and tasks from the macOS calendar database.
More information: <https://hasseg.org/icalBuddy/>.

- Show events later today:

`icalBuddy -n eventsToday`

- Show uncompleted tasks:

`icalBuddy uncompletedTasks`

- Show a formatted list separated by calendar for all events today:

`icalBuddy -f -sc eventsToday`

- Show tasks for a specified number of days:

`icalBuddy -n tasksDueBefore:today+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">days</span>

- Show events in a time range:

`icalBuddy eventsFrom:'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_date</span>`' to:'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_date</span>`'`
