---
layout: page
title: osx/dmesg (English)
description: "Write the kernel messages to `stdout`."
content_hash: 537b8c79d747281bb8ebbc1fe343aa6940451c6b
last_modified_at: 2024-01-31
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/osx/dmesg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dmesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dmesg

Write the kernel messages to `stdout`.
More information: <https://keith.github.io/xcode-man-pages/dmesg.8.html>.

- Show kernel messages:

`dmesg`

- Show how much physical memory is available on this system:

`dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`dmesg | less`
