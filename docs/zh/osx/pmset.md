---
layout: page
title: osx/pmset (中文)
description: "配置 macOS 电源管理设置，就像在系统首选项 > 节能程序中一样。"
content_hash: 22ffe693fa049e0b0e8bdb4afc8b0098c8caeb50
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/pmset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pmset

配置 macOS 电源管理设置，就像在系统首选项 > 节能程序中一样。
修改设置的命令必须以 `sudo` 开头。
更多信息：<https://keith.github.io/xcode-man-pages/pmset.1.html>.

- 显示当前电源管理设置：

`pmset -g`

- 显示当前电源和电池电量：

`pmset -g batt`

- 立即让显示器进入休眠状态：

`pmset displaysleepnow`

- 当充电器通电时，将显示器设置为从不休眠：

`sudo pmset -c displaysleep 0`

- 使用电池电源 15 分钟后将显示器设置为休眠：

`sudo pmset -b displaysleep 15`

- 安排计算机在每个工作日上午 9 点自动唤醒：

`sudo pmset repeat wake MTWRF 09:00:00`

- 还原为系统默认值：

`sudo pmset -a displaysleep 10 disksleep 10 sleep 30 womp 1`
