---
layout: page
title: common/bcomps (中文)
description: "将图形分解为它们的双连通分量。"
content_hash: d11b644e5dee94796ddccbd04a31fe67d816bfb6
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/bcomps.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bcomps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bcomps

将图形分解为它们的双连通分量。
Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
更多信息：<https://graphviz.org/pdf/bcomps.1.pdf>.

- 将一个或多个图形分解为它们的双连通分量：

`bcomps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 打印一个或多个图形中的块和切割顶点的数量：

`bcomps -v -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>

- 根据 `输出.gv` 将每个块和块切割顶点树写入多个有编号的文件中：

`bcomps -x -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv 路径/到/输入2.gv ...</span>

- 显示 `bcomps` 的帮助信息：

`bcomps -?`
