---
layout: page
title: common/adb-reverse (中文)
description: "安卓调试桥-反射： 反向映射安卓模拟器实例或者已连接的实体设备的套接字连接。"
content_hash: cea2da4adce90573bb7b4a0638d63f746eb45d3c
related_topics:
  - title: English version
    url: /en/common/adb-reverse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-reverse.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-reverse.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-reverse.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-reverse.html
    icon: bi bi-globe
---
# adb reverse

安卓调试桥-反射： 反向映射安卓模拟器实例或者已连接的实体设备的套接字连接。
更多信息：<https://developer.android.com/studio/command-line/adb>.

- 列出所有来自模拟器和设备的映射连接：

`adb reverse --list`

- 将 TCP 端口从安卓模拟器或设备中映射到 localhost：

`adb reverse tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程端口</span>` tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">本地端口</span>

- 从安卓模拟器或设备移除一个反向 socket 连接：

`adb reverse --remove tcp:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程端口</span>

- 从安卓模拟器或设备移除所有反向 socket 连接：

`adb reverse --remove-all`
