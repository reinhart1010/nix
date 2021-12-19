---
layout: page
title: android/pm (中文)
description: "显示关于 Android 设备上的应用程序的信息。"
content_hash: 1c43fa8e97663984489d784e9bc92787170b5d40
related_topics:
  - title: Deutsch version
    url: /de/android/pm.html
    icon: bi bi-globe
  - title: English version
    url: /en/android/pm.html
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
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/android/pm.html
    icon: bi bi-globe
---
# pm

显示关于 Android 设备上的应用程序的信息。
更多信息：<https://developer.android.com/studio/command-line/adb#pm>.

- 打印所有已安装应用程序的列表：

`pm list packages`

- 打印所有已安装的系统应用程序的列表：

`pm list packages -s`

- 打印所有已安装的第三方应用程序的列表：

`pm list packages -3`

- 打印与指定关键字匹配的应用程序列表：

`pm list packages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>

- 打印指定应用的 APK 的路径：

`pm path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名</span>
