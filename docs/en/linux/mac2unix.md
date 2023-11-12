---
layout: page
title: linux/mac2unix (English)
description: "Change macOS-style line endings to Unix-style."
content_hash: a78adb72c15bf876c86dc8bff12cabea7c88bdec
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/linux/mac2unix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mac2unix

Change macOS-style line endings to Unix-style.
Replaces CR with LF.
More information: <https://waterlan.home.xs4all.nl/dos2unix.html>.

- Change the line endings of a file:

`mac2unix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Create a copy with Unix-style line endings:

`mac2unix -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_filename</span>
