---
layout: page
title: linux/xclock (English)
description: "Display the time in analog or digital form."
content_hash: a7361c7e4efe277ba4b2379df86f6604a7f6f4e5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# xclock

Display the time in analog or digital form.
More information: <https://manned.org/xclock>.

- Display an analog clock:

`xclock`

- Display a 24-hour digital clock with the hour and minute fields only:

`xclock -digital -brief`

- Display a digital clock using an strftime format string (see strftime(3)):

`xclock -digital -strftime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>

- Display a 24-hour digital clock with the hour, minute and second fields that updates every second:

`xclock -digital -strftime '%H:%M:%S' -update 1`

- Display a 12-hour digital clock with the hour and minute fields only:

`xclock -digital -twelve -brief`
