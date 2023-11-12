---
layout: page
title: linux/lsb_release (中文)
description: "提供某些 LSB（Linux 标准库）和特定于发行版的信息。"
content_hash: 318c29d32bd7dd7a0a0f4d7d326948830b7016e5
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/lsb_release.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/lsb_release.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/lsb_release.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lsb_release.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsb_release

提供某些 LSB（Linux 标准库）和特定于发行版的信息。
更多信息：<https://manned.org/lsb_release>.

- 打印所有可用信息：

`lsb_release -a`

- 打印操作系统的描述（通常是全名）：

`lsb_release -d`

- 仅打印操作系统名称 (ID)，隐藏字段名称：

`lsb_release -i -s`

- 打印发行版的版本号和代号，隐藏字段名称：

`lsb_release -rcs`
