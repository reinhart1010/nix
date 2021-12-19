---
layout: page
title: linux/lsusb (English)
description: "Display information about USB buses and devices connected to them."
content_hash: 4253c98e1d63770302709f0024de970d7f50fb13
related_topics:
  - title: español version
    url: /es/linux/lsusb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/lsusb.html
    icon: bi bi-globe
---
# lsusb

Display information about USB buses and devices connected to them.
More information: <https://manned.org/lsusb>.

- List all the USB devices available:

`lsusb`

- List the USB hierarchy as a tree:

`lsusb -t`

- List verbose information about USB devices:

`lsusb --verbose`

- List detailed information about a USB device:

`lsusb -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- List devices with a specified vendor and product ID only:

`lsusb -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vendor</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product</span>
