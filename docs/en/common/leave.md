---
layout: page
title: common/leave (English)
description: "Set a reminder for when it's time to leave."
content_hash: e5e26edaff6162ccda42db7fba2413c314f1a3b0
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# leave

Set a reminder for when it's time to leave.
To remove reminders use `kill $(pidof leave)`.
More information: <https://www.freebsd.org/cgi/man.cgi?query=leave>.

- Set a reminder at a given time:

`leave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time_to_leave</span>

- Set a reminder to leave at noon:

`leave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1200</span>

- Set a reminder in a specific amount of time:

`leave +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amount_of_time</span>

- Set a reminder to leave in 4 hours and 4 minutes:

`leave +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0404</span>
