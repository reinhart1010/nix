---
layout: page
title: osx/caffeinate (中文)
description: "防止 Mac 进入休眠模式。"
content_hash: dc0d2dedef234d7c52ff5de39fda806e2a6e3cbd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/caffeinate.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/caffeinate.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/caffeinate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/caffeinate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/caffeinate.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/caffeinate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/caffeinate.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># caffeinate

防止 Mac 进入休眠模式。
更多信息：<https://ss64.com/osx/caffeinate.html>.

- 防止进入休眠模式 , 1 小时内（3600 秒）：

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- 在指定命令执行完前，禁止进入休眠：

`caffeinate -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 在你按 Ctrl-C 之前禁止进入休眠模式：

`caffeinate -i`
