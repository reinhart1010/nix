---
layout: page
title: linux/iostat (English)
description: "Report statistics for devices and partitions."
content_hash: 3cdb68fb08b6628838bfdf3c37f0801e59ec469b
---
# iostat

Report statistics for devices and partitions.
More information: <https://manned.org/iostat>.

- Display a report of CPU and disk statistics since system startup:

`iostat`

- Display a report of CPU and disk statistics with units converted to megabytes:

`iostat -m`

- Display CPU statistics:

`iostat -c`

- Display disk statistics with disk names (including LVM):

`iostat -N`

- Display extended disk statistics with disk names for device "sda":

`iostat -xN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sda</span>

- Display incremental reports of CPU and disk statistics every 2 seconds:

`iostat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>
