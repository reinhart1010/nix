---
layout: page
title: linux/udevadm (English)
description: "Linux `udev` management tool."
content_hash: 6aa602fba67e729f143422c41429719d9e2f09f7
---
# udevadm

Linux `udev` management tool.
More information: <https://www.freedesktop.org/software/systemd/man/udevadm>.

- Monitor all device events:

`sudo udevadm monitor`

- Print `uevents` sent out by the kernel:

`sudo udevadm monitor --kernel`

- Print device events after being processed by `udev`:

`sudo udevadm monitor --udev`

- List attributes of a device:

`sudo udevadm info --attribute-walk --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- Reload all `udev` rules:

`sudo udevadm control --reload-rules`

- Trigger all `udev` rules to run:

`sudo udevadm trigger`
