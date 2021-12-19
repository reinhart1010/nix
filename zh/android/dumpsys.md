---
layout: page
title: android/dumpsys (中文)
description: "提供关于 Android 系统服务的信息。"
content_hash: 0acccf1dc3dacca9cd297f434bac6708789e4624
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
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/dumpsys.html
    icon: bi bi-globe
---
# dumpsys

提供关于 Android 系统服务的信息。
此命令只能通过 `adb shell` 使用。
更多信息：<https://developer.android.com/studio/command-line/dumpsys>.

- 获取所有系统服务的诊断输出：

`dumpsys`

- 获取指定系统服务的诊断输出：

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务</span>

- 列出 `dumpsys` 可以提供的所有服务信息：

`dumpsys -l`

- 列出服务的指定服务参数：

`dumpsys `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务</span>` -h`

- 从诊断输出中排除指定服务：

`dumpsys --skip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务</span>

- 指定超时时间，以秒为单位（默认为 10s）：

`dumpsys -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒数</span>
