---
layout: page
title: linux/timedatectl (English)
description: "Control the system time and date."
content_hash: b20af1c4bde2c36431669042ef3e27e8bc365405
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/linux/timedatectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# timedatectl

Control the system time and date.
More information: <https://manned.org/timedatectl>.

- Check the current system clock time:

`timedatectl`

- Set the local time of the system clock directly:

`timedatectl set-time "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yyyy-MM-dd hh:mm:ss</span>`"`

- List available timezones:

`timedatectl list-timezones`

- Set the system timezone:

`timedatectl set-timezone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timezone</span>

- Enable Network Time Protocol (NTP) synchronization:

`timedatectl set-ntp on`

- Change the hardware clock time standard to localtime:

`timedatectl set-local-rtc 1`
