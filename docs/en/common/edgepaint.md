---
layout: page
title: common/edgepaint (English)
description: "Colorize edges of a graph layout to clarify crossing edges."
content_hash: 476bd4b12f8985bf2d36fc91320ba92e6239f926
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/common/edgepaint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# edgepaint

Colorize edges of a graph layout to clarify crossing edges.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://graphviz.org/pdf/edgepaint.1.pdf>.

- Colorize edges of one or more graph layouts (that already have layout information) to clarify crossing edges:

`edgepaint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/layout1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/layout2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Colorize edges using a color scheme. (See <https://graphviz.org/doc/info/colors.html#brewer>):

`edgepaint -color-scheme=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">accent7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/layout.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Lay out a graph and colorize its edges, then convert to a PNG image:

`dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>` | edgepaint | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Display help:

`edgepaint -?`
