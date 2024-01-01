---
layout: page
title: common/eval (中文)
description: "在当前 shell 中以单个命令的形式执行参数，并返回其结果。"
content_hash: 94a352c91deb9aae95e86c0e09bf3aea8d7f920c
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/eval.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eval

在当前 shell 中以单个命令的形式执行参数，并返回其结果。
更多信息：<https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#eval>.

- 使用 'foo' 做为参数调用 `echo`：

`eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo foo</span>`"`

- 在当前 shell 程序中设置变量：

`eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo=bar</span>`"`
