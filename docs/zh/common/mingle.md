---
layout: page
title: common/mingle (中文)
description: "捆绑图形布局中的边缘。"
content_hash: a2c92ab166b8233bc312176d05945506febce5b5
last_modified_at: 2023-02-17
related_topics:
  - title: English version
    url: /en/common/mingle.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mingle

捆绑图形布局中的边缘。
Graphviz 过滤器：`acyclic`、`bcomps`、`comps`、`edgepaint`、`gvcolor`、`gvpack`、`mingle`、`nop`、`sccmap`、`tred` 和 `unflatten`。
更多信息： <https://www.graphviz.org/pdf/mingle.1.pdf>.

- 捆绑一个或多个已经有布局信息的图形布局的边缘：

`mingle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/布局1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/布局2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.gv</span>

- 通过一个命令执行布局、捆绑和输出到图片：

`dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入.gv</span>` | mingle | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.png</span>

- 显示 `mingle` 的帮助信息：

`mingle -?`
