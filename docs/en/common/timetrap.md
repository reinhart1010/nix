---
layout: page
title: common/timetrap (English)
description: "Simple command-line time tracker written in Ruby."
content_hash: bb37b754e69e0044d62a5ff18cbfdddd4545ecce
last_modified_at: 2023-08-20
---
# timetrap

Simple command-line time tracker written in Ruby.
More information: <https://github.com/samg/timetrap>.

- Create a new timesheet:

`timetrap sheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timesheet</span>

- Check in an entry started 5 minutes ago:

`timetrap in --at "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 minutes ago</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">entry_notes</span>

- Display the current timesheet:

`timetrap display`

- Edit the last entry's end time:

`timetrap edit --end `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time</span>
