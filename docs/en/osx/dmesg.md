---
layout: page
title: osx/dmesg (English)
description: "Write the kernel messages to `stdout`."
content_hash: c324c40d97a490ebe51897dbcad8534702d862c5
last_modified_at: 2023-08-09
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dmesg.html
    icon: bi bi-globe
---
# dmesg

Write the kernel messages to `stdout`.
More information: <https://www.manpagez.com/man/8/dmesg/>.

- Show kernel messages:

`dmesg`

- Show how much physical memory is available on this system:

`dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`dmesg | less`
