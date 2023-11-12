---
layout: page
title: linux/debootstrap (中文)
description: "创建一个基本的 `Debian` 系统。"
content_hash: 4b6e2265bb0b0fb84d75688e54e5a7be4695a8ae
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/debootstrap.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/debootstrap.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># debootstrap

创建一个基本的 `Debian` 系统。
更多信息：<https://wiki.debian.org/Debootstrap>.

- 在 `debian-root` 目录中创建一个 `Debian` 稳定分支系统：

`sudo debootstrap stable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/debian-root/</span>` http://deb.debian.org/debian`

- 使用本地镜像在 `focal-root` 目录中创建一个 `Ubuntu 20.04` 系统：

`sudo debootstrap focal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/focal-root/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file:///path/to/mirror/</span>

- 切换到可引导系统：

`sudo chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root</span>

- 列出可用的版本：

`ls /usr/share/debootstrap/scripts/`
