---
layout: page
title: linux/unix2mac (English)
description: "Change Unix-style line endings to macOS-style."
content_hash: 46597f6c2cfa83f08cba7a7c64e8e2109a4a7696
last_modified_at: 2023-05-18
related_topics:
  - title: 中文 version
    url: /zh/linux/unix2mac.html
    icon: bi bi-globe
---
# unix2mac

Change Unix-style line endings to macOS-style.
Replaces LF with CR.
More information: <https://waterlan.home.xs4all.nl/dos2unix.html>.

- Change the line endings of a file:

`unix2mac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a copy with macOS-style line endings:

`unix2mac -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/unix_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mac_file</span>
