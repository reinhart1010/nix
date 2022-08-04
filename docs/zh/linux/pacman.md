---
layout: page
title: linux/pacman (中文)
description: "Arch Linux 的软件包管理器工具。"
content_hash: 56e34eb60310c5b99e320c10ea68ed2488ff3916
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
---
# pacman

Arch Linux 的软件包管理器工具。
更多信息：<https://man.archlinux.org/man/pacman.8>.

- 同步并更新所有软件包：

`sudo pacman --sync --refresh --sysupgrade`

- 安装一个新的软件包：

`sudo pacman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 删除一个软件包及其依赖：

`sudo pacman --remove --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 在软件包数据库中搜索正则表达式或关键字：

`pacman --sync --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>`"`

- 列出已安装的软件包和版本：

`pacman --query`

- 仅列出明确安装的软件包和版本：

`pacman --query --explicit`

- 查找哪个包拥有某个文件：

`pacman --query --owns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 清空软件包缓存以释放空间：

`sudo pacman --sync --clean --clean`
