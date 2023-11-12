---
layout: page
title: linux/telinit (English)
description: "Change SysV runlevel."
content_hash: 1886afe1d0dd38a6f8426666e70edebe52a4f83e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# telinit

Change SysV runlevel.
Since the concept SysV runlevels is obsolete the runlevel requests will be transparently translated into systemd unit activation requests.
More information: <https://manned.org/telinit>.

- Power off the machine:

`telinit 0`

- Reboot the machine:

`telinit 6`

- Change SysV run level:

`telinit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|3|4|5</span>

- Change to rescue mode:

`telinit 1`

- Reload daemon configuration:

`telinit q`

- Do not send a wall message before reboot/power-off (6/0):

`telinit --no-wall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>
