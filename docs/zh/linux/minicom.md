---
layout: page
title: linux/minicom (中文)
description: "与设备的串行接口进行通信。"
content_hash: ca211c9c0e4b1370fb3ee6d9439406516bbe8012
last_modified_at: 2024-11-28
related_topics:
  - title: English version
    url: /en/linux/minicom.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/minicom.html
    icon: bi bi-globe
tldri18n_status: 2
---
# minicom

与设备的串行接口进行通信。
更多信息：<https://manned.org/minicom>.

- 打开给定的串行端口：

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>

- 以给定的波特率打开给定的串行端口：

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --baudrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- 在与给定串行端口通信前进入配置菜单：

`sudo minicom --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --setup`
