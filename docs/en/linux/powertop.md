---
layout: page
title: linux/powertop (English)
description: "Optimize battery power usage."
content_hash: eb8d374a66f62e37cdd19557921443e79604b46b
last_modified_at: 2023-08-17
related_topics:
  - title: polski version
    url: /pl/linux/powertop.html
    icon: bi bi-globe
---
# powertop

Optimize battery power usage.
More information: <https://github.com/fenrus75/powertop>.

- Calibrate power usage measurements:

`sudo powertop --calibrate`

- Generate HTML power usage report in the current directory:

`sudo powertop --html=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">power_report.html</span>

- Tune to optimal settings:

`sudo powertop --auto-tune`

- Generate a report for a specified number of seconds (instead of 20 by default):

`sudo powertop --time=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
