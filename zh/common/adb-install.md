---
layout: page
title: common/adb-install (中文)
description: "安卓调试桥 -Install: 将应用安装包推送到 Android 模拟器或已连接的安卓设备。"
content_hash: e21378650c09ee823178b965b601eb2d970968f7
related_topics:
  - title: English version
    url: /en/common/adb-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-install.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-install.html
    icon: bi bi-globe
---
# adb install

安卓调试桥 -Install: 将应用安装包推送到 Android 模拟器或已连接的安卓设备。
更多信息：<https://developer.android.com/studio/command-line/adb>.

- 向模拟器/设备推送安卓 app:

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 重装 app, 保持原有数据：

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 授予 app manifest 中列举的所有权限许可：

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 快速部署模式，仅更新 APK 更改过的部分：

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>
