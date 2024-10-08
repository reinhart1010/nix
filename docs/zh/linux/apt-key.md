---
layout: page
title: linux/apt-key (中文)
description: "Debian 和 Ubuntu 上的 APT 软件包管理器的密钥管理工具。"
content_hash: 381262f93de4f6077455e5f7bb6a6f813448d3cc
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-key.html
    icon: bi bi-globe
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
  - title: polski version
    url: /pl/linux/apt-key.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-key.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-key

Debian 和 Ubuntu 上的 APT 软件包管理器的密钥管理工具。
更多信息：<https://manned.org/apt-key.8>.

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
