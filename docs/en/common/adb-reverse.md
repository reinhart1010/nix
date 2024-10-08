---
layout: page
title: common/adb-reverse (English)
description: "Reverse socket connections from a connected Android device or emulator."
content_hash: 81947dc63d1e23bac27b51bc826d6649503a07d6
last_modified_at: 2024-10-08
related_topics:
  - title: español version
    url: /es/common/adb-reverse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-reverse.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-reverse.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb-reverse.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-reverse.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-reverse.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-reverse.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-reverse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb reverse

Reverse socket connections from a connected Android device or emulator.
More information: <https://developer.android.com/tools/adb>.

- List all reverse socket connections from emulators and devices:

`adb reverse --list`

- Reverse a TCP port from an emulator or device to localhost:

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>

- Remove a reverse socket connections from an emulator or device:

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- Remove all reverse socket connections from all emulators and devices:

`adb reverse --remove-all`
