---
layout: page
title: linux/systool (English)
description: "View system device information by bus, and classes."
content_hash: 679089bb94a2e3960558a75b80bd6716d056d6fe
last_modified_at: 2024-06-22
tldri18n_status: 2
---
# systool

View system device information by bus, and classes.
This command is part of the `sysfs` package.
More information: <https://github.com/linux-ras/sysfsutils>.

- List all attributes of devices of a bus (eg. `pci`, `usb`). View all buses using `ls /sys/bus`:

`systool -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus</span>` -v`

- List all attributes of a class of devices (eg. `drm`, `block`). View all classes using `ls /sys/class`:

`systool -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class</span>` -v`

- Show only device drivers of a bus (eg. `pci`, `usb`):

`systool -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus</span>` -D`
