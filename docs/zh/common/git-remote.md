---
layout: page
title: common/git-remote (中文)
description: "管理跟踪的远程仓库（remotes）。"
content_hash: 359a2497919d3ecdaa161bfe884ed7ecaf4974d4
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-remote.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-remote.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-remote.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-remote.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-remote.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-remote.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-remote.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-remote.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-remote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git remote

管理跟踪的远程仓库（remotes）。
更多信息：<https://git-scm.com/docs/git-remote>.

- 列出已经存在的远程仓库，包括它们的名字和 URL：

`git remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>

- 查看某个远程仓库的信息：

`git remote show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程仓库名字</span>

- 添加远程仓库：

`git remote add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程仓库名字</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程仓库 URL</span>

- 更改远程仓库地址链接（使用 `--add` 选项不会移除现有的 URL）：

`git remote set-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程仓库名字</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新 URL</span>

- 查看远程仓库的 URL：

`git remote get-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程仓库名字</span>

- 移除远程仓库：

`git remote remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程仓库名字</span>

- 重命名远程仓库：

`git remote rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">旧名字</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新名字</span>
