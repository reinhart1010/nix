---
layout: page
title: common/git-clone (中文)
description: "克隆现有的代码库。"
content_hash: 72b9329cc3e34dcbbca1a5d6bd7cf8016d1f7151
last_modified_at: 2024-01-02
related_topics:
  - title: Deutsch version
    url: /de/common/git-clone.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-clone.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clone.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clone.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clone.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clone.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clone.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-clone.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clone.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clone.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-clone.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git clone

克隆现有的代码库。
更多信息：<https://git-scm.com/docs/git-clone>.

- 克隆一个现有的代码库到指定文件夹：

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程代码库地址</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件夹</span>

- 克隆一个现有的代码库和它的子模块：

`git clone --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程代码库地址</span>

- 克隆一个本地的代码库：

`git clone --local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/本地/代码库名</span>

- 静默克隆，不打印任何日志：

`git clone --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程代码库地址</span>

- 克隆一个现有的代码库，只获取默认分支上10个最新的提交（对节省时间很有用）：

`git clone --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程代码库地址</span>

- 克隆一个现有的、特定远程分支的代码库：

`git clone --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分支名称</span>` --single-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程代码库地址</span>

- 使用 SSH 命令克隆一个现有的代码库：

`git clone --config core.sshCommand="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh -i 路径/到/ssh_私钥</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程代码库地址</span>
