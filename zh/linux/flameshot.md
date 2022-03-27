---
layout: page
title: linux/flameshot (中文)
description: "带有 gui 界面的 Screenshot 工具，支持基本的图像编辑，例如文本，形状，颜色和 imgur."
content_hash: 347a88e4feb73485a089de3f8189c33723e9cfee
related_topics:
  - title: English version
    url: /en/linux/flameshot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/flameshot.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/flameshot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># flameshot

带有 gui 界面的 Screenshot 工具，支持基本的图像编辑，例如文本，形状，颜色和 imgur.
更多信息：<https://flameshot.org>.

- 在 GUI 模式下启动 Flameshot：

`flameshot launcher`

- 通过单击并拖动来截取屏幕截图：

`flameshot gui`

- 全屏截图：

`flameshot full`

- 将保存屏幕快照的路径设置为：

`flameshot full --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 将屏幕截图延迟 2000 毫秒，然后输出到剪贴板：

`flameshot full --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2000</span>` --clipboard`
