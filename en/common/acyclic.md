---
layout: page
title: common/acyclic (English)
description: "Make a directed graph acyclic by reversing some edges."
content_hash: 4a35b60f4c6e950e0e15e8fb2738e620905afac4
---
# acyclic

Make a directed graph acyclic by reversing some edges.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://graphviz.org/pdf/acyclic.1.pdf>.

- Make a directed graph acyclic by reversing some edges:

`acyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Print if a graph is acyclic, has a cycle, or is undirected, producing no output graph:

`acyclic -v -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>

- Display help for `acyclic`:

`acyclic -?`
