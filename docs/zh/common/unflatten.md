---
layout: page
title: common/unflatten (中文)
description: "调整有向图以改善布局的纵横比。"
content_hash: 48c5ecf03416c3c42d3e015edf88356693f59606
last_modified_at: 2023-02-17
related_topics:
  - title: English version
    url: /en/common/unflatten.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># unflatten

调整有向图以改善布局的纵横比。
Graphviz 过滤器: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, 和 `unflatten`。
更多信息: <https://www.graphviz.org/pdf/unflatten.1.pdf>.

- 调整一个或多个有向图以改善布局的纵横比:

`unflatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 将 `unflatten` 作为 `dot` 布局的预处理器以改善纵横比:

`unflatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入.gv</span>` | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.png</span>

- 显示 `unflatten` 的帮助:

`unflatten -?`