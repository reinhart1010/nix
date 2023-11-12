---
layout: page
title: common/airmon-ng (中文)
description: "激活无线网络设备的监控模式。"
content_hash: 7cd1dd239f7fc01608e013718034844ec0371809
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/airmon-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/airmon-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airmon-ng.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airmon-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airmon-ng.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airmon-ng.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/airmon-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airmon-ng

激活无线网络设备的监控模式。
更多信息：<https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- 列出无线设备和它们的状态：

`sudo airmon-ng`

- 为一个特定的设备打开监控模式：

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- 关闭使用无线设备的干扰进程：

`sudo airmon-ng check kill`

- 关闭某个特定网络接口的监控模式：

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
