---
layout: page
title: linux/bluetoothctl (中文)
description: "从命令行管理蓝牙设备。"
content_hash: 05c3ba7ad0ab7b3d3174ce88a5669b745ca1b532
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bluetoothctl.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bluetoothctl

从命令行管理蓝牙设备。
更多信息：<https://bitbucket.org/serkanp/bluetoothctl>.

- 进入 bluetoothctl 外壳程序：

`bluetoothctl`

- 列出设备：

`bluetoothctl -- devices`

- 与一个设备配对：

`bluetoothctl -- pair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac 地址</span>

- 移除一个设备：

`bluetoothctl -- remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac 地址</span>

- 连接一个已配对的设备：

`bluetoothctl -- connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac 地址</span>

- 断开一个已配对的设备：

`bluetoothctl -- disconnect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac 地址</span>
