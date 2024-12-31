---
layout: page
title: common/timew (English)
description: "A time tracking tool used to measure the duration of activities."
content_hash: 8c5e62bca8eec6c4a58473dcb3b71f97dc941381
last_modified_at: 2024-12-31
related_topics:
  - title: 한국어 version
    url: /ko/common/timew.html
    icon: bi bi-globe
tldri18n_status: 2
---
# timew

A time tracking tool used to measure the duration of activities.
More information: <https://timewarrior.net/docs>.

- Start tracking an activity:

`timew start`

- Tag the current activity:

`timew tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activity_tag</span>

- Start tracking and tag a new activity:

`timew start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activity_tag</span>

- Stop the current activity:

`timew stop`

- Track an activity in the past:

`timew track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_time} - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_time</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activity_tag</span>

- View tracked items of the day:

`timew summary`

- View report for the last day, week, current month, etc.:

`timew summary :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today|yesterday|week|lastweek|month|lastmonth|year|lastyear</span>
