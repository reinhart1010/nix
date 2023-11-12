---
layout: page
title: common/adb-install (中文)
description: "安卓调试桥 -Install: 将应用安装包推送到 Android 模拟器或已连接的安卓设备。"
content_hash: 6690a04c6d6a4e9b1611423daa692d485956f288
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/adb-install.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/adb-install.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-install.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adb-install.html
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
tldri18n_status: 2
---
# adb install

安卓调试桥 -Install: 将应用安装包推送到 Android 模拟器或已连接的安卓设备。
更多信息：<https://developer.android.com/studio/command-line/adb>.

- 向模拟器/设备推送安卓 app：

`adb install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 向特定的模拟器/设备推送安卓 app（覆盖 `$ANDROID_SERIAL`）：

`adb -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">序列号</span>` install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 重装 app, 保持原有数据：

`adb install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 推送一个允许版本代码降级的安卓 app（仅适用于可调试的软件包）：

`adb install -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 授予 app manifest 中列举的所有权限许可：

`adb install -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>

- 快速部署模式，仅更新 APK 更改过的部分：

`adb install --fastdeploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/应用.apk</span>
