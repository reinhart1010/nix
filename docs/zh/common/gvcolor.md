---
layout: page
title: common/gvcolor (中文)
description: "用一系列颜色为有序有向图着色。"
content_hash: df671a9d78a20e805829be137bb97102524893f8
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/gvcolor.html
    icon: bi bi-globe
---
# gvcolor

用一系列颜色为有序有向图着色。
Graphviz 过滤器: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`。
更多信息: <https://graphviz.org/pdf/gvcolor.1.pdf>.

- 为一个或多个已被 `dot` 处理的有序有向图着色:

`gvcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/布局1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/布局2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 对一个图进行布局和着色，然后将其转换为 PNG 图像:

`dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入.gv</span>` | gvcolor | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.png</span>

- 显示 `gvcolor` 的帮助信息:

`gvcolor -?`
