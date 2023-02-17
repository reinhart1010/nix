---
layout: page
title: common/tred (中文)
description: "计算有向图的传递闭包约简。"
content_hash: 384e950e051ef5a85281f24bd558351284a4b520
last_modified_at: 2023-02-17
related_topics:
  - title: English version
    url: /en/common/tred.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tred

计算有向图的传递闭包约简。
Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
更多信息： <https://www.graphviz.org/pdf/tred.1.pdf>.

- 构建一个或多个有向图的传递闭包约简：

`tred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 显示帮助信息：

`tred -?`