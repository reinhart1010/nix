---
layout: page
title: common/ccomps (English)
description: "Decompose graphs into their connected components."
content_hash: ce5ea259ee799dbea66138cac1efb02151a709e6
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/common/ccomps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ccomps

Decompose graphs into their connected components.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://graphviz.org/pdf/ccomps.1.pdf>.

- Decompose one or more graphs into their connected components:

`ccomps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Print the number of nodes, edges, and connected components in one or more graphs:

`ccomps -v -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>

- Write each connected component to numbered filenames based on `output.gv`:

`ccomps -x -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>

- Display help:

`ccomps -?`
