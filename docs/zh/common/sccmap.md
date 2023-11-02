---
layout: page
title: common/sccmap (中文)
description: "提取有向图的强连通分量。"
content_hash: 56244ce863421e7b8b92083e0984cb5b7f386382
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/common/sccmap.html
    icon: bi bi-globe
---
# sccmap

提取有向图的强连通分量。
Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
更多信息：<https://www.graphviz.org/pdf/sccmap.1.pdf>.

- 从一个或多个有向图中提取强连通分量：

`sccmap -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 打印一个图形的统计信息，不生成输出图形：

`sccmap -v -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>

- 显示 `sccmap` 的帮助信息：

`sccmap -?`
