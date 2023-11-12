---
layout: page
title: linux/zypper (中文)
description: "SUSE & openSUSE 的软件包管理工具。"
content_hash: 87c8932e4f8da68d15d3230c9be02d5263e3479e
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/zypper.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/zypper.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/zypper.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/zypper.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/zypper.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/zypper.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/zypper.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zypper

SUSE & openSUSE 的软件包管理工具。
更多信息：<https://en.opensuse.org/SDB:Zypper_manual>.

- 同步可用的软件包和版本列表：

`zypper refresh`

- 安装一个新的软件包：

`zypper install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 移除一个软件包：

`zypper remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 将已安装的软件包升级到最新的可用版本：

`zypper update`

- 通过关键字搜索软件包：

`zypper search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键字</span>
