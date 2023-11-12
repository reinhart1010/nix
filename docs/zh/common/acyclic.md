---
layout: page
title: common/acyclic (中文)
description: "通过反转一些边来使有向图无环。"
content_hash: 0553ff0c6e2ee5c6955fd26e65e95e414313e01c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/acyclic.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/acyclic.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acyclic.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acyclic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# acyclic

通过反转一些边来使有向图无环。
Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
更多信息：<https://graphviz.org/pdf/acyclic.1.pdf>.

- 通过反转一些边来使有向图无环：

`acyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 打印出一个图是无环的、有环的还是无向的，不产生输出图：

`acyclic -v -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入.gv</span>

- 显示 `acyclic` 的帮助：

`acyclic -?`
