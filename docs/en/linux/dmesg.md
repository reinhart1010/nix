---
layout: page
title: linux/dmesg (English)
description: "Write the kernel messages to `stdout`."
content_hash: 6d2c950042b21f1fe5f90b58d61c8c9da7b156d1
last_modified_at: 2024-09-30
related_topics:
  - title: català version
    url: /ca/linux/dmesg.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmesg.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Write the kernel messages to `stdout`.
More information: <https://manned.org/dmesg>.

- Show kernel messages:

`sudo dmesg`

- Show kernel error messages:

`sudo dmesg --level err`

- Show kernel messages and keep reading new ones, similar to `tail -f` (available in kernels 3.5.0 and newer):

`sudo dmesg -w`

- Show how much physical memory is available on this system:

`sudo dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`sudo dmesg | less`

- Show kernel messages with a timestamp (available in kernels 3.5.0 and newer):

`sudo dmesg -T`

- Show kernel messages in human-readable form (available in kernels 3.5.0 and newer):

`sudo dmesg -H`

- Colorize output (available in kernels 3.5.0 and newer):

`sudo dmesg -L`
