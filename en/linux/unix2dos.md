---
layout: page
title: linux/unix2dos (English)
description: "Change Unix-style line endings to DOS-style."
content_hash: f2acf45299295b0e2d14088a54870c86a721ebf9
related_topics:
  - title: 中文 version
    url: /zh/linux/unix2dos.html
    icon: bi bi-globe
---
# unix2dos

Change Unix-style line endings to DOS-style.
Replaces CR with CRLF.
More information: <https://waterlan.home.xs4all.nl/dos2unix.html>.

- Change the line endings of a file:

`unix2dos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Create a copy with DOS-style line endings:

`unix2dos -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_filename</span>
