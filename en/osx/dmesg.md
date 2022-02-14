---
layout: page
title: osx/dmesg (English)
description: "Write the kernel messages to standard output."
content_hash: f86f15d23a053d28149e88de1a9d4c3194f7bb68
related_topics:
  - title: 中文 version
    url: /zh/osx/dmesg.html
    icon: bi bi-globe
---
# dmesg

Write the kernel messages to standard output.
More information: <https://www.manpagez.com/man/8/dmesg/>.

- Show kernel messages:

`dmesg`

- Show how much physical memory is available on this system:

`dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`dmesg | less`
