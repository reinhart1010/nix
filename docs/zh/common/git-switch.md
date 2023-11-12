---
layout: page
title: common/git-switch (中文)
description: "切换 Git 分支。要求 Git 版本在 2.23 以上。"
content_hash: ede82ebea36344ec707f43919c77df6d6d075545
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-switch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-switch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-switch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-switch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-switch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-switch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git switch

切换 Git 分支。要求 Git 版本在 2.23 以上。
另请参阅 `git checkout`。
更多信息：<https://git-scm.com/docs/git-switch>.

- 切换到一个已有的分支：

`git switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分支名字</span>

- 创建并切换到一个新分支：

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分支名字</span>

- 创建并切换到基于某个提交的新分支：

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分支名字</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定提交</span>

- 切换到之前的分支：

`git switch -`

- 切换到一个分支，并更新所有匹配的子模块：

`git switch --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分支名字</span>

- 切换到一个分支，并和当前分支以及暂未提交的修改进行三方合并：

`git switch --merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">分支名字</span>
