---
layout: page
title: linux/bluetoothctl (中文)
description: "从命令行管理蓝牙设备。"
content_hash: 05c3ba7ad0ab7b3d3174ce88a5669b745ca1b532
related_topics:
  - title: English version
    url: /en/linux/bluetoothctl.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/bluetoothctl.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/bluetoothctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
