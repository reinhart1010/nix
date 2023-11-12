---
layout: page
title: linux/brightnessctl (中文)
description: "GUN/Linux 操作系统上用来读取和控制设备亮度的实用工具。"
content_hash: b33e3f1e518e88cf316678e7e006179f3f0b6b7e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/brightnessctl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/brightnessctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/brightnessctl.html
    icon: bi bi-globe
tldri18n_status: 2
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

`brightnessctl set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10%-</span>
