---
layout: page
title: linux/brightnessctl (中文)
description: "GUN/Linux 操作系统上用来读取和控制设备亮度的实用工具。"
content_hash: 61e228f2f9651e4cbde6defc4dc26be7f8495cb5
related_topics:
  - title: English version
    url: /en/linux/brightnessctl.html
    icon: bi bi-globe
---
# brightnessctl

GUN/Linux 操作系统上用来读取和控制设备亮度的实用工具。
更多信息：<https://github.com/Hummer12007/brightnessctl>.

- 列出亮度可变的设备：

`brightnessctl --list`

- 打印显示器当前亮度：

`brightnessctl get`

- 将显示器背光的亮度设置为指定的百分比：

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50%</span>

- 按指定的增量增加亮度：

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+10%</span>

- 将亮度降低指定的递减量：

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10%</span>
