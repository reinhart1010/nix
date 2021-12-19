---
layout: page
title: linux/arch-chroot (中文)
description: "辅助 Arch Linux 安装流程的更强 `chroot` 命令。"
content_hash: 0703e59bf2beaeeb310881ab40b763689c2f9fdb
related_topics:
  - title: Deutsch version
    url: /de/linux/arch-chroot.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/arch-chroot.html
    icon: bi bi-globe
---
# arch-chroot

辅助 Arch Linux 安装流程的更强 `chroot` 命令。
更多信息：<https://man.archlinux.org/man/arch-chroot.8>.

- 在新的根目录下开启一个交互外壳程序（默认是 `bash`）：

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新根目录</span>

- 指定除当前用户外的其他用户来运行外壳程序：

`arch-chroot -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新根目录</span>

- 在新的根目录下运行一个自定义命令（取代默认的 `bash`）：

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新根目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令参数</span>

- 指定除默认的 `bash` 以外的外壳程序（以下例子需要现在目标系统中先安装 `zsh`）：

`arch-chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新根目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zsh</span>
