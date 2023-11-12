---
layout: page
title: linux/aura (中文)
description: "Aura 包管理器：一个安全且支持多语言的 Arch Linux 和 AUR 的包管理器。"
content_hash: b33346104b31324c6ab93857d39820c0c250c76e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/aura.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aura

Aura 包管理器：一个安全且支持多语言的 Arch Linux 和 AUR 的包管理器。
更多信息：<https://github.com/fosskers/aura>.

- 从官方仓库和 AUR 检索包：

`aura --aursync --both --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名|正则</span>

- 从 AUR 安装一个软件包：

`aura --aursync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 以详细模式升级所有的 AUR 包并移除所有的编译依赖：

`aura --aursync --diff --sysupgrade --delmakedeps --unsuppress`

- 从官方仓库安装一个软件包：

`aura --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 同步并更新官方仓库的所有软件包：

`aura --sync --refresh --sysupgrade`

- 使用包缓存降级一个软件包：

`aura --downgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 移除一个软件包及其依赖：

`aura --remove --recursive --unneeded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 移除孤儿包（作为依赖安装但现在不被任何包依赖）：

`aura --orphans --abandon`
