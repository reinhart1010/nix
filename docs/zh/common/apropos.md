---
layout: page
title: common/apropos (中文)
description: "在 manpages 中搜索，例如查找一个新命令。"
content_hash: 95f3eaece86cf582bc5fdde01e99afda0a2033f7
last_modified_at: 2024-11-27
related_topics:
  - title: Deutsch version
    url: /de/common/apropos.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/apropos.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/apropos.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/apropos.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/apropos.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apropos.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apropos.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apropos

在 manpages 中搜索，例如查找一个新命令。
更多信息：<https://manned.org/apropos>.

- 使用正则表达式搜索关键字：

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式</span>

- 搜索时不限制输出到终端宽度：

`apropos -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式</span>

- 搜索与给定的所有表达式都匹配的页面：

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式_1</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式_2</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式_3</span>
