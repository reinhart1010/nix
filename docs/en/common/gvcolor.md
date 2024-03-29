---
layout: page
title: common/gvcolor (English)
description: "Colorize a ranked digraph with a range of colors."
content_hash: 17731cecb32a9b8e3fa8a4424574811332a46b5e
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/common/gvcolor.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gvcolor

Colorize a ranked digraph with a range of colors.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://graphviz.org/pdf/gvcolor.1.pdf>.

- Colorize one or more ranked digraph (that were already processed by `dot`):

`gvcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/layout1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/layout2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Lay out a graph and colorize it, then convert to a PNG image:

`dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>` | gvcolor | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Display help:

`gvcolor -?`
