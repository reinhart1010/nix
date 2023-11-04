---
layout: page
title: common/nop (中文)
description: "检查有效性并以规范的格式漂亮地打印图形。"
content_hash: 5547079355a578672b385eb839298ff8784975b4
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/nop.html
    icon: bi bi-globe
---
# nop

检查有效性并以规范的格式漂亮地打印图形。
Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
更多信息： <https://www.graphviz.org/pdf/nop.1.pdf>.

- 漂亮地打印一个或多个规范格式的图形：

`nop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 检查一个或多个图形的有效性，不生成输出图形：

`nop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>

- 显示 `nop` 的帮助信息：

`nop -?`
