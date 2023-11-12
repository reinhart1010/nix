---
layout: page
title: linux/flameshot (中文)
description: "带有 GUI 界面的 Screenshot 工具。"
content_hash: 410ea6b8803f4c3eb50e57e4025028aa903298fe
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/flameshot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/flameshot.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/flameshot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# flameshot

带有 GUI 界面的 Screenshot 工具。
支持基本的图像编辑，例如文本，形状，颜色和 imgur。
更多信息：<https://flameshot.org>.

- 全屏截图：

`flameshot full`

- 交互式截图：

`flameshot gui`

- 截图并保存到特定的路径：

`flameshot gui --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 简单模式下交互式截图：

`flameshot launcher`

- 指定屏幕截图：

`flameshot screen --number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 截图并打印到标准输出：

`flameshot gui --raw`

- 截图并复制到剪切板：

`flameshot gui --clipboard`

- 延迟指定毫秒时间截图：

`flameshot full --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5000</span>
