---
layout: page
title: common/edgepaint (中文)
description: "对图形布局的边缘进行着色，以澄清交叉边缘。"
content_hash: 2e1049b08115484aa50ce8df1f0c438d12a0b5f8
last_modified_at: 2023-02-17
related_topics:
  - title: English version
    url: /en/common/edgepaint.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># edgepaint

对图形布局的边缘进行着色，以澄清交叉边缘。
Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
更多信息：<https://graphviz.org/pdf/edgepaint.1.pdf>.

- 对一个或多个已经有布局信息的图形布局的边缘进行着色，以澄清交叉边缘：

`edgepaint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/布局1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/布局2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 使用颜色方案对边缘进行着色。（参见：<https://graphviz.org/doc/info/colors.html#brewer>）：

`edgepaint -color-scheme=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">accent7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/布局.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 对图形进行布局并对其边缘进行着色，然后将其转换为 PNG 图像：

`dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入.gv</span>` | edgepaint | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.png</span>

- 显示 `edgepaint` 的帮助信息：

`edgepaint -?`
