---
layout: page
title: linux/lsusb (English)
description: "Display information about USB buses and devices connected to them."
content_hash: e2ea2a138566dd5d0311cf64cff1644ce55f0f34
last_modified_at: 2023-07-18
related_topics:
  - title: català version
    url: /ca/linux/lsusb.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/lsusb.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/lsusb.html
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

`lsusb --verbose -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device number</span>

- List devices with a specified vendor and product ID only:

`lsusb -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vendor</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product</span>
