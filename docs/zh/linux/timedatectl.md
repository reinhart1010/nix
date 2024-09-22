---
layout: page
title: linux/timedatectl (中文)
description: "控制系统时间和日期。"
content_hash: f7120c71f09a301a32e42026f4aa2d771bfdc9b7
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/linux/timedatectl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/timedatectl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# timedatectl

控制系统时间和日期。
更多信息：<https://manned.org/timedatectl>.

- 检查当前系统时钟时间：

`timedatectl`

- 直接设置系统时钟的本地时间：

`timedatectl set-time "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yyyy-MM-dd hh:mm:ss</span>`"`

- 列出可用时区：

`timedatectl list-timezones`

- 设置系统时区：

`timedatectl set-timezone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">时区</span>

- 启用网络时间协议（NTP）同步：

`timedatectl set-ntp on`

- 将硬件时钟时间标准更改为本地时间：

`timedatectl set-local-rtc 1`
