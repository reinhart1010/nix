---
layout: page
title: linux/partprobe (English)
description: "Notify the operating system kernel of partition table changes."
content_hash: d711109409d40cb0b31ac40e538f969ecae35568
---
# partprobe

Notify the operating system kernel of partition table changes.
More information: <https://manned.org/partprobe>.

- Notify the operating system kernel of partition table changes:

`sudo partprobe`

- Notify the kernel of partition table changes and show a summary of devices and their partitions:

`sudo partprobe --summary`

- Show a summary of devices and their partitions but don't notify the kernel:

`sudo partprobe --summary --dry-run`
