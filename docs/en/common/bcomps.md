---
layout: page
title: common/bcomps (English)
description: "Decompose graphs into their biconnected components."
content_hash: 85b7c920056abf49d3cbfad2348387494899f4a9
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/common/bcomps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bcomps

Decompose graphs into their biconnected components.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://graphviz.org/pdf/bcomps.1.pdf>.

- Decompose one or more graphs into their biconnected components:

`bcomps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Print the number of blocks and cutvertices in one or more graphs:

`bcomps -v -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>

- Write each block and block-cutvertex tree to multiple numbered filenames based on `output.gv`:

`bcomps -x -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>

- Display help:

`bcomps -?`
