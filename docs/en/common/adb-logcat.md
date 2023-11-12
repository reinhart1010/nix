---
layout: page
title: common/adb-logcat (English)
description: "Dump a log of system messages."
content_hash: 23d8e711a26f5c1db9d568e13cd3cb44957854ee
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/adb-logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-logcat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-logcat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb logcat

Dump a log of system messages.
More information: <https://developer.android.com/studio/command-line/logcat>.

- Display system logs:

`adb logcat`

- Display lines that match a regular expression:

`adb logcat -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>

- Display logs for a tag in a specific mode ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent), filtering other tags:

`adb logcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mode</span>` *:S`

- Display logs for React Native applications in [V]erbose mode [S]ilencing other tags:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Display logs for all tags with priority level [W]arning and higher:

`adb logcat *:W`

- Display logs for a specific PID:

`adb logcat --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Display logs for the process of a specific package:

`adb logcat --pid=$(adb shell pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`)`

- Color the log (usually use with filters):

`adb logcat -v color`
