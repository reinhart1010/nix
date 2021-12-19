---
layout: page
title: linux/xclock (English)
description: "Display the time in analog or digital form."
content_hash: 3e4d2600b1b5fe2f4e3590bed453e0f2d2c3fcf6
---
# xclock

Display the time in analog or digital form.

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
