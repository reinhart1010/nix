---
layout: page
title: linux/yay (中文)
description: "Yet Another Yogurt: 一个用于 Arch Linux 的工具，用于从 Arch User Repository 中构建和安装软件包。"
content_hash: 216d9b66b4161eec31761e8c9e5f1ddc3de684eb
related_topics:
  - title: Deutsch version
    url: /de/linux/yay.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/yay.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/yay.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/yay.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/yay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yay

Yet Another Yogurt: 一个用于 Arch Linux 的工具，用于从 Arch User Repository 中构建和安装软件包。
另见 `pacman`。
更多信息：<https://github.com/Jguer/yay>.

- 从仓库和 AUR 中交互式搜索和安装软件包：

`yay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包|搜索词</span>

- 同步并更新所有来自仓库和 AUR 的软件包：

`yay`

- 只同步和更新 AUR 软件包：

`yay -Sua`

- 从仓库和 AUR 中安装一个新的软件包：

`yay -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 从仓库和 AUR 中搜索软件包数据库中的关键词：

`yay -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>

- 显示已安装软件包和系统健康状况的统计数据：

`yay -Ps`
