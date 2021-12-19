---
layout: page
title: android/dumpsys (中文 (繁體, 台灣))
description: "提供關於 Android 系統服務的資訊。"
content_hash: 572a587fe20fe78d2a5f5014ab81928dff308806
related_topics:
  - title: Deutsch version
    url: /de/android/dumpsys.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/dumpsys.html
    icon: bi bi-globe
  - title: français version
    url: /fr/android/dumpsys.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/android/dumpsys.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/android/dumpsys.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/android/dumpsys.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/android/dumpsys.html
    icon: bi bi-globe
---
# dumpsys

提供關於 Android 系統服務的資訊。
此命令只能透過 `adb shell` 使用。
更多資訊：<https://developer.android.com/studio/command-line/dumpsys>.

- 獲取所有系統服務的診斷輸出：

`dumpsys`

- 獲取指定系統服務的診斷輸出：

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服務</span>

- 列出 `dumpsys` 可以提供的所有服務資訊：

`dumpsys -l`

- 列出服務的指定服務引數：

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服務</span>` -h`

- 從診斷輸出中排除指定服務：

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服務</span>

- 指定超時時間，以秒為單位（預設為 10 秒）：

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒數</span>
