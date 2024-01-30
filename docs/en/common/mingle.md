---
layout: page
title: common/mingle (English)
description: "Bundle the edges of a graph layout."
content_hash: 99a6eca2748c853ca2d421bb3b1f35feb4eb2152
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/common/mingle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mingle

Bundle the edges of a graph layout.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://www.graphviz.org/pdf/mingle.1.pdf>.

- Bundle the edges of one or more graph layouts (that already have layout information):

`mingle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/layout1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/layout2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Perform layout, bundling, and output to a picture with one command:

`dot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>` | mingle | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Display help:

`mingle -?`
