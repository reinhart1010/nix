---
layout: page
title: osx/dmesg (English)
description: "Write the kernel messages to standard output."
content_hash: f9e8efbf4628a40298aaf733f32b9f44d5d6298f
related_topics:
  - title: 中文 version
    url: /zh/osx/dmesg.html
    icon: bi bi-globe
---
# dmesg

Write the kernel messages to standard output.

- Show kernel messages:

`dmesg`

- Show how much physical memory is available on this system:

`dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`dmesg | less`
