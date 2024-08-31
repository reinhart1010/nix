---
layout: page
title: common/fastboot (中文)
description: "在引导加载程序模式下与连接的 Android 设备通信（在这里无法使用 ADB）。"
content_hash: 3f68412b0706ef44409d0b9bc282d8d0dc1209f8
last_modified_at: 2024-08-31
related_topics:
  - title: English version
    url: /en/common/fastboot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/fastboot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fastboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fastboot

在引导加载程序模式下与连接的 Android 设备通信（在这里无法使用 ADB）。
更多信息：<https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>.

- 解锁引导加载程序：

`fastboot oem unlock`

- 回锁引导加载程序：

`fastboot oem lock`

- 从 fastboot 模式再次重启到 fastboot 模式：

`fastboot reboot bootloader`

- 刷入镜像：

`fastboot flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.img</span>

- 刷入自定义恢复镜像：

`fastboot flash recovery `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.img</span>

- 列出已连接的设备：

`fastboot devices`

- 列出设备所有信息：

`fastboot getvar all`
