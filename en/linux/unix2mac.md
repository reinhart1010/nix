---
layout: page
title: linux/unix2mac (English)
description: "Change Unix-style line endings to macOS-style."
content_hash: c48b0bd2a59e990c243b271306b8a782d9400e81
related_topics:
  - title: 中文 version
    url: /zh/linux/unix2mac.html
    icon: bi bi-globe
---
# unix2mac

Change Unix-style line endings to macOS-style.
Replaces CR with LF.
More information: <https://waterlan.home.xs4all.nl/dos2unix.html>.

- Change the line endings of a file:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Create a copy with macOS-style line endings:

`unix2mac -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_filename</span>
