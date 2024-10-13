---
layout: page
title: linux/auracle (中文)
description: "用来和 Arch Linux 用户仓库交互的命令行工具，这个仓库通常被称作 AUR."
content_hash: 96c9ad2ed65bc760027b6d082fe748406dd3c434
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/linux/auracle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# auracle

用来和 Arch Linux 用户仓库交互的命令行工具，这个仓库通常被称作 AUR.
更多信息：<https://github.com/falconindy/auracle>.

- 显示符合一个正则表达式的 AUR 包：

`auracle search '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`'`

- 显示 AUR 包列表的包信息，包名以一个单独的空格分隔：

`auracle info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- 显示 AUR 包列表的 `PKGBUILD` 文件（编译信息），包名以一个单独的空格分隔：

`auracle show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package1 package2 ...</span>

- 显示已安装 AUR 包的更新：

`auracle outdated`
