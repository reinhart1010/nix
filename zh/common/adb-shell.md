---
layout: page
title: common/adb-shell (中文)
description: "安卓调试桥-Shell: 运行安卓模拟器或者连接设备上的远程终端命令。"
content_hash: d11ea87e19126cb808bbd316010e59e63e2478f4
related_topics:
  - title: English version
    url: /en/common/adb-shell.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/adb-shell.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/adb-shell.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/adb-shell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/adb-shell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adb-shell.html
    icon: bi bi-globe
---
# adb shell

安卓调试桥-Shell: 运行安卓模拟器或者连接设备上的远程终端命令。
更多信息：<https://developer.android.com/studio/command-line/adb>.

- 启动模拟器/设备上的远程终端：

`adb shell`

- 获取模拟器/设备全部属性：

`adb shell getprop`

- 重置所有运行时权限为它们的默认值：

`adb shell pm reset-permissions`

- 撤销一个应用的危险权限：

`adb shell pm revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">权限</span>

- 触发一个键盘敲击事件：

`adb shell input keyevent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键位码</span>

- 清除模拟器/设备上的数据：

`adb shell pm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 启动模拟器/设备上的一个行为：

`adb shell am start -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">活动名</span>

- 启动模拟器/设备上的首页活动：

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
