---
layout: page
title: linux/apt-key (中文)
description: "Debian 和 Ubuntu 上的 APT 软件包管理器的密钥管理工具。"
content_hash: cbca97e17fdc318f1f5aa801ae3e82d0e10da05c
related_topics:
  - title: Deutsch version
    url: /de/linux/apt-key.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-key.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-key.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-key.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-key.html
    icon: bi bi-globe
---
# apt-key

Debian 和 Ubuntu 上的 APT 软件包管理器的密钥管理工具。
更多信息：<https://manpages.debian.org/latest/apt/apt-key.8.html>.

- 列出可信密钥：

`apt-key list`

- 向可信密钥库中添加一个密钥：

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密钥文件.asc</span>

- 从可信密钥库中移除一个密钥：

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密钥 id</span>

- 向可信密钥库中添加一个远程密钥：

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://host.tld/filename.key</span>` | apt-key add -`

- 指定密钥 ID, 从密钥服务器中添加一个密钥：

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密钥 id</span>
