---
layout: page
title: linux/aurman (中文)
description: "用来构建和安装 AUR 包的 Arch Linux 实用工具。"
content_hash: b7de5838c8569749475652f293a0ffb26f4aa77a
related_topics:
  - title: English version
    url: /en/linux/aurman.html
    icon: bi bi-globe
---
# aurman

用来构建和安装 AUR 包的 Arch Linux 实用工具。
参见 `pacman`.
更多信息：<https://github.com/polygamma/aurman>.

- 同步并更新所有包：

`aurman --sync --refresh --sysupgrade`

- 同步并更新所有包但不显示 `PKGBUILD` 文件的变动：

`aurman --sync --refresh --sysupgrade --noedit`

- 安装一个新包：

`aurman --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 安装一个新包但不显示 `PKGBUILD` 文件的变动：

`aurman --sync --noedit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 无确认提示安装一个新包：

`aurman --sync --noedit --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 在官方仓库和 AUR 的包数据库中查找关键字：

`aurman --sync --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键字</span>

- 移除一个包及其依赖：

`aurman --remove --recursive --nosave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 清除包缓存（用两次 `--clean` 参数清除所有包缓存）：

`aurman --sync --clean`
