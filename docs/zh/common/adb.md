---
layout: page
title: common/adb (中文)
description: "安卓调试桥：与 Android 模拟器或已连接的 Android 设备通信。"
content_hash: 5a27ad009e3f53e8c8882cc205301b22770434ae
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/adb.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/adb.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adb

安卓调试桥：与 Android 模拟器或已连接的 Android 设备通信。
此命令也有关于其子命令的文件，例如：`shell`.
更多信息：<https://developer.android.com/tools/adb>.

- 检查 adb server 进程的是否在运行，并开启它：

`adb start-server`

- 终止 adb server 进程：

`adb kill-server`

- 在目标模拟器 / 设备实例上开启一个远程 shell：

`adb shell`

- 将 Android 应用程序推送到模拟器 / 设备：

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 从目标设备上拷贝一个文件 / 目录到本地：

`adb pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/设备的文件或目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/本地上的目录</span>

- 从本地拷贝一个文件 / 目录到目标设备：

`adb push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/本地文件或目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/设备上的目录</span>

- 列出已连接的设备：

`adb devices`
