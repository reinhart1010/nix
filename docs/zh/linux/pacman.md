---
layout: page
title: linux/pacman (中文)
description: "Arch Linux 的软件包管理器工具。"
content_hash: ec58d345a513397c0ef8189aa222d4b60a76b2e2
last_modified_at: 2023-05-16
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
  - title: Indonesia version
    url: /id/linux/pacman.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/pacman.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/pacman.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman.html
    icon: bi bi-globe
---
# pacman

Arch Linux 的软件包管理器工具。
也可以看看：`pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`,  `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
更多信息：<https://man.archlinux.org/man/pacman.8>.

- 同步并更新所有软件包：

`sudo pacman -Syu`

- 安装一个新的软件包：

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 删除一个软件包及其依赖：

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 在软件包数据库中搜索正则表达式或关键字：

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>`"`

- 列出已安装的软件包和版本：

`pacman -Q`

- 仅列出明确安装的软件包和版本：

`pacman -Qe`

- 查找哪个包拥有某个文件：

`pacman -Qo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 清空软件包缓存以释放空间：

`sudo pacman -Scc`
