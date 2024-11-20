---
layout: page
title: common/qdbus (中文)
description: "进程间通信 (IPC) 和远程过程调用 (RPC) 机制，最初在 Linux 上开发。"
content_hash: 7dfcb76e91931a0a6e66504db194436bea4ed2ef
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/qdbus.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qdbus.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qdbus

进程间通信 (IPC) 和远程过程调用 (RPC) 机制，最初在 Linux 上开发。
更多信息：<https://doc.qt.io/qt-5/qtdbus-index.html>.

- 列出可用的服务名称：

`qdbus`

- 列出指定服务的对象路径：

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务名</span>

- 列出指定对象可用的方法、信号和属性：

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/对象</span>

- 执行指定方法，传递参数并显示返回值：

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/对象</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">方法名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">参数1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">参数2</span>

- 显示在 KDE Plasma 会话中的当前亮度值：

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/org/kde/Solid/PowerManagement/Actions/BrightnessControl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness</span>

- 设置 KDE Plasma 会话中的特定亮度：

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/org/kde/Solid/PowerManagement/Actions/BrightnessControl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>

- 在 KDE Plasma 会话中调用音量增大快捷键：

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.kglobalaccel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/component/kmix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invokeShortcut</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">increase_volume</span>`"`

- 优雅地注销并然后选择不执行任何操作、重启或关机：

`qdbus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.kde.Shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Shutdown</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">logout|logoutAndReboot|logoutAndShutdown</span>
