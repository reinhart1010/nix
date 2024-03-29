---
layout: page
title: common/sccmap (English)
description: "Extract strongly connected components of directed graphs."
content_hash: e569efca3098424a251db73541c08f3a4bf853ff
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/common/sccmap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sccmap

Extract strongly connected components of directed graphs.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://www.graphviz.org/pdf/sccmap.1.pdf>.

- Extract strongly connected components of one or more directed graphs:

`sccmap -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Print statistics about a graph, producing no output graph:

`sccmap -v -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>

- Display help:

`sccmap -?`
