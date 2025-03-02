---
layout: page
title: common/julia (中文)
description: "一种用于技术计算的高层次、高性能动态编程语言。"
content_hash: b5f1ea95af79fa915b4d7ed8442b86c281f8918e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/julia.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/julia.html
    icon: bi bi-globe
tldri18n_status: 2
---
# julia

一种用于技术计算的高层次、高性能动态编程语言。
更多信息：<https://docs.julialang.org/en/v1/manual/getting-started/>.

- 启动一个 REPL（交互式 shell）：

`julia`

- 执行一个 Julia 程序并退出：

`julia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program.jl</span>

- 执行一个带有参数的 Julia 程序：

`julia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program.jl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">参数</span>

- 执行包含 Julia 代码的字符串：

`julia -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">julia_代码</span>`'`

- 执行一段 Julia 代码，并向其传递参数：

`julia -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">for x in ARGS; println(x); end</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">参数</span>

- 计算一个表达式并打印结果：

`julia -E '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(1 - cos(pi/4))/2</span>`'`

- 以多线程模式启动 Julia，使用 N 个线程：

`julia -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>
