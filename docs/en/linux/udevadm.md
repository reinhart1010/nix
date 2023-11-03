---
layout: page
title: linux/udevadm (English)
description: "Linux `udev` management tool."
content_hash: 381ac2afa6208a3e10250d6f0b95ccbe807ebaf7
last_modified_at: 2023-11-03
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

- List attributes of device `/dev/sda`:

`sudo udevadm info --attribute-walk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- Reload all `udev` rules:

`sudo udevadm control --reload-rules`

- Trigger all `udev` rules to run:

`sudo udevadm trigger`

- Test an event run by simulating loading of `/dev/sda`:

`sudo udevadm test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>
