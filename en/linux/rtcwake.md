---
layout: page
title: linux/rtcwake (English)
description: "Enter a system sleep state until specified wakeup time relative to your BIOS clock."
content_hash: 6ed9baae6e5682326c73f497a30b51e2dffda056
---
# rtcwake

Enter a system sleep state until specified wakeup time relative to your BIOS clock.
More information: <https://manned.org/rtcwake>.

- Show whether an alarm is set or not:

`sudo rtcwake -m show -v`

- Suspend to RAM and wakeup after 10 seconds:

`sudo rtcwake -m mem -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Suspend to disk (higher power saving) and wakeup 15 minutes later:

`sudo rtcwake -m disk --date +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15</span>`min`

- Freeze the system (more efficient than suspend-to-RAM but version 3.9 or newer of the Linux kernel is required) and wakeup at a given date and time:

`sudo rtcwake -m freeze --date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDDhhmm</span>

- Disable a previously set alarm:

`sudo rtcwake -m disable`

- Perform a dry run to wakeup the computer at a given time. (Press Ctrl + C to abort):

`sudo rtcwake -m on --date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:ss</span>
