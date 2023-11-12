---
layout: page
title: common/ccomps (中文)
description: "将图形分解为它们的连通分量。"
content_hash: 7433c8a310d6bcb1f0a9cf52a580fc53bcb4dfea
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ccomps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ccomps

将图形分解为它们的连通分量。
Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
更多信息：<https://graphviz.org/pdf/ccomps.1.pdf>.

- 将一个或多个图形分解为它们的连通分量：

`ccomps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 打印一个或多个图形中的节点、边和连通分量的数量：

`ccomps -v -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>

- 根据 `输出.gv` 将每个连通分量写入多个有编号的文件中：

`ccomps -x -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>

- 显示 `ccomps` 的帮助信息：

`ccomps -?`
