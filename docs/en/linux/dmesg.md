---
layout: page
title: linux/dmesg (English)
description: "Write the kernel messages to `stdout`."
content_hash: f4feb8c8b8bc1aa55a46ade12db5fe8c4e7e7ddd
last_modified_at: 2023-08-09
related_topics:
  - title: català version
    url: /ca/linux/dmesg.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dmesg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dmesg.html
    icon: bi bi-globe
---
# dmesg

Write the kernel messages to `stdout`.
More information: <https://manned.org/dmesg>.

- Show kernel messages:

`dmesg`

- Show kernel error messages:

`dmesg --level err`

- Show kernel messages and keep reading new ones, similar to `tail -f` (available in kernels 3.5.0 and newer):

`dmesg -w`

- Show how much physical memory is available on this system:

`dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`dmesg | less`

- Show kernel messages with a timestamp (available in kernels 3.5.0 and newer):

`dmesg -T`

- Show kernel messages in human-readable form (available in kernels 3.5.0 and newer):

`dmesg -H`

- Colorize output (available in kernels 3.5.0 and newer):

`dmesg -L`
