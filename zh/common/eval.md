---
layout: page
title: common/eval (中文)
description: "在当前 shell 中以单个命令的形式执行参数，并返回其结果。"
content_hash: b96020c22b081a1d84d61fc1db1a8e8d9dbb89fa
related_topics:
  - title: English version
    url: /en/common/eval.html
    icon: bi bi-globe
---
# eval

在当前 shell 中以单个命令的形式执行参数，并返回其结果。
更多信息：<https://manned.org/eval>.

- 使用 'foo' 做为参数调用 `echo`：

`eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo foo</span>`"`

- 在当前 shell 程序中设置变量：

`eval "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo=bar</span>`"`
