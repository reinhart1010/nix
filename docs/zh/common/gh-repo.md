---
layout: page
title: common/gh-repo (中文)
description: "在命令行上操作 GitHub 仓库。"
content_hash: 2d596b89dae5d40c746ad3f5996926cac47a4c44
last_modified_at: 2024-11-28
related_topics:
  - title: English version
    url: /en/common/gh-repo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gh-repo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gh repo

在命令行上操作 GitHub 仓库。
更多信息：<https://cli.github.com/manual/gh_repo>.

- 创建一个新的仓库（如果没有设置仓库名称，默认将为当前目录的名称）：

`gh repo create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 克隆一个仓库：

`gh repo clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">拥有者</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">仓库</span>

- 复刻并克隆一个仓库：

`gh repo fork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">拥有者</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">仓库</span>` --clone`

- 在默认的网络浏览器中查看一个仓库：

`gh repo view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">仓库</span>` --web`

- 列出特定用户或组织拥有的仓库（如果未设置拥有者，默认拥有者将是当前登录用户）：

`gh repo list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">拥有者</span>

- 仅列出非派生的仓库，并限制列出的仓库数量（默认：30）：

`gh repo list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">拥有者</span>` --source -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">限制数量</span>

- 列出具有特定主要编程语言的仓库：

`gh repo list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">拥有者</span>` --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">语言名称</span>
