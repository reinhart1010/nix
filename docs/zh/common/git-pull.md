---
layout: page
title: common/git-pull (中文)
description: "从远程代码库拉取分支，并将其合并到本地代码库。"
content_hash: 1c46348f22042558c549301601e5542982c54cb8
related_topics:
  - title: Deutsch version
    url: /de/common/git-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pull.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-pull.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pull.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git pull

从远程代码库拉取分支，并将其合并到本地代码库。
更多信息：<https://git-scm.com/docs/git-pull>.

- 从默认的远程分支中拉取代码并执行合并：

`git pull`

- 使用快进功能（快进到含义为：先清空暂存区，再执行合并，最后恢复暂存区），从默认的远程分支拉取代码并执行合并：

`git pull --rebase`

- 从给定的分支中拉取代码，并执行合并到对应分支：

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程分支名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">本地分支名</span>
