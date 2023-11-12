---
layout: page
title: common/git (中文)
description: "分布式版本控制系统。"
content_hash: d31bb6acaf250704b1c1d6c0c008ba7a049f4f32
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/git.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/git.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/git.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git

分布式版本控制系统。
类似如 `commit`、`add`、`branch`、`checkout`、`push` 等子命令都有自己的使用文档，可以通过 `tldr git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">子命令</span> 的形式查阅。
更多信息：<https://git-scm.com/>.

- 检查 git 的版本号：

`git --version`

- 显示帮助文档：

`git --help`

- 显示 git 子命令的详细帮助文档（如 `clone`, `add`, `push`, `log` 等子命令）：

`git help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">子命令</span>

- 执行 git 的子命令：

`git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">子命令</span>

- 在自定义的 git 仓库根路径下执行子命令：

`git -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">仓库地址</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">子命令</span>

- 在给定参数条件下，执行 git 的子命令：

`git -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置项</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">子命令</span>
