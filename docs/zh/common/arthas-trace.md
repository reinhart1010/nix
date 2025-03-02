---
layout: page
title: common/arthas-trace (中文)
description: "方法内部调用路径，并输出方法路径上的每个节点上耗时。"
content_hash: 02cb47386186b922d9c66dce7554bc58f1674827
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/arthas-trace.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arthas-trace

方法内部调用路径，并输出方法路径上的每个节点上耗时。
另见 `arthas`, `arthas-watch`.
更多信息：<https://arthas.aliyun.com/en/doc/trace.html>.

- 追踪方法调用链：

`trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>

- 追踪方法调用链，仅显示大于 10 毫秒的调用：

`trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>` '#cost > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`'`

- 追踪多个类和方法的调用：

`trace -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern1|class-patter2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern1|method-pattern2|method-pattern3</span>

- 仅显示大于 10 毫秒的调用链，观测 10 次：

`trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">class-pattern</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method-pattern</span>` '#cost > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`' -n 5`
