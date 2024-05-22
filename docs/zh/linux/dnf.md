---
layout: page
title: linux/dnf (中文)
description: "RHEL, Fedora 和 CentOS 的软件包管理工具（yum 的替代品）。"
content_hash: eaa770ba1eecc6c3c72e2f32181978bb3cc9d6be
last_modified_at: 2024-05-22
related_topics:
  - title: català version
    url: /ca/linux/dnf.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dnf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dnf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/dnf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/dnf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnf

RHEL, Fedora 和 CentOS 的软件包管理工具（yum 的替代品）。
对于其他包管理器中的等效命令，请见 <https://wiki.archlinux.org/title/Pacman/Rosetta>.
更多信息：<https://dnf.readthedocs.io>.

- 更新已安装的包到最新可用版本：

`sudo dnf upgrade`

- 通过关键词搜索包：

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词1 关键词2 ...</span>

- 显示软件包的描述：

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包</span>

- 安装软件包（使用 `-y` 自动确认所有提示）：

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包1 包2 ...</span>

- 删除软件包：

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包1 包2 ...</span>

- 列出已安装的包：

`dnf list --installed`

- 查找哪些包提供给定命令：

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 查看所有过去的操作：

`dnf history`
