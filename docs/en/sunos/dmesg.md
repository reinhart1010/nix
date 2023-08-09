---
layout: page
title: sunos/dmesg (English)
description: "Write the kernel messages to `stdout`."
content_hash: 1e562a09ee1f2317bf23f66bf6efa719d1b8f641
last_modified_at: 2023-08-09
related_topics:
  - title: français version
    url: /fr/sunos/dmesg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/dmesg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/dmesg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/sunos/dmesg.html
    icon: bi bi-globe
---
# dmesg

Write the kernel messages to `stdout`.
More information: <https://www.unix.com/man-page/sunos/1m/dmesg>.

- Show kernel messages:

`dmesg`

- Show how much physical memory is available on this system:

`dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`dmesg | less`
