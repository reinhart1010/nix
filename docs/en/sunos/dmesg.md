---
layout: page
title: sunos/dmesg (English)
description: "Write the kernel messages to standard output."
content_hash: ad27e28a81bad857849f5065f0c242c543bc9cbb
related_topics:
  - title: 中文 version
    url: /zh/sunos/dmesg.html
    icon: bi bi-globe
---
# dmesg

Write the kernel messages to standard output.
More information: <https://www.unix.com/man-page/sunos/1m/dmesg>.

- Show kernel messages:

`dmesg`

- Show how much physical memory is available on this system:

`dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`dmesg | less`
