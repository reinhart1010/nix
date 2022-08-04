---
layout: page
title: android/logcat (English)
description: "Dump a log of system messages."
content_hash: 8defe27182c757a7a1bcb1b53aafaf8453704a9c
related_topics:
  - title: Deutsch version
    url: /de/android/logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/logcat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/logcat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/logcat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/logcat.html
    icon: bi bi-globe
---
# logcat

Dump a log of system messages.
More information: <https://developer.android.com/studio/command-line/logcat>.

- Display system logs:

`logcat`

- Write system logs to a file:

`logcat -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display lines that match a regular expression:

`logcat --regex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>
