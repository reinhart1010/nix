---
layout: page
title: linux/paru (中文)
description: "一个 AUR 助手和 pacman 包装。"
content_hash: b47b25ff7b25d4577bb284567ba9180e10535d5d
last_modified_at: 2024-01-01
related_topics:
  - title: Deutsch version
    url: /de/linux/paru.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/paru.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/paru.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paru

一个 AUR 助手和 pacman 包装。
更多信息：<https://github.com/Morganamilo/paru>.

- 交互式搜索并安装软件包：

`paru `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名或关键字</span>

- 同步和更新所有包：

`paru`

- 更新 AUR 包：

`paru -Sua`

- 获取包的信息：

`paru -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包</span>

- 从 AUR 或 ABS 下载 `PKGBUILD` 和其他的包的源文件：

`paru --getpkgbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包</span>

- 显示包的 `PKGBUILD` 文件：

`paru --getpkgbuild --print `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包</span>
