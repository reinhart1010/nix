---
layout: page
title: android/pm (English)
description: "Show information about apps on an Android device."
content_hash: 9d3d3babbf2ef636f3ed3f94a817f89ff8e8d0a3
related_topics:
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/pm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/pm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/pm.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/pm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---
# pm

Show information about apps on an Android device.
More information: <https://developer.android.com/studio/command-line/adb#pm>.

- Print a list of all installed apps:

`pm list packages`

- Print a list of all installed system apps:

`pm list packages -s`

- Print a list of all installed 3rd-Party apps:

`pm list packages -3`

- Print a list of apps matching specific keywords:

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keywords</span>

- Print the path of the APK of a specific app:

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app</span>
