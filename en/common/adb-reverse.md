---
layout: page
title: common/adb-reverse (English)
description: "Android Debug Bridge Reverse: reverse socket connections from an Android emulator instance or connected Android devices."
content_hash: 4fc730c1a0f6da354b4f0d884ee2de0bb7bec20b
related_topics:
  - title: Indonesia version
    url: /id/common/adb-reverse.html
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
---
# adb reverse

Android Debug Bridge Reverse: reverse socket connections from an Android emulator instance or connected Android devices.
More information: <https://developer.android.com/studio/command-line/adb>.

- List all reverse socket connections from emulators and devices:

`adb reverse --list`

- Reverse a TCP port from an emulator or device to localhost:

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>

- Remove a reverse socket connections from an emulator or device:

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- Remove all reverse socket connections from all emulators and devices:

`adb reverse --remove-all`
