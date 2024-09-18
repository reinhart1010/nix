---
layout: page
title: linux/apt-add-repository (中文)
description: "管理 APT 仓库。"
content_hash: 58ee3796feb2de1986b7ad21917c23bb0a0c545e
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-add-repository.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-add-repository

管理 APT 仓库。
更多信息：<https://manned.org/apt-add-repository.1>.

- 添加一个 APT 仓库：

`apt-add-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- 移除一个 APT 仓库：

`apt-add-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- 添加一个 APT 仓库之后更新包缓存：

`apt-add-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>

- 开启源码包：

`apt-add-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_spec</span>
