---
layout: page
title: linux/udevadm (English)
description: "Linux `udev` management tool."
content_hash: b275ecdf3096822511ccb72abaf05a7aafe18ade
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/udevadm.html
    icon: bi bi-globe
tldri18n_status: 2
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

`sudo udevadm control --reload`

- Trigger all `udev` rules to run:

`sudo udevadm trigger`

- Test an event run by simulating loading of `/dev/sda`:

`sudo udevadm test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>
