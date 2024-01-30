---
layout: page
title: common/acyclic (English)
description: "Make a directed graph acyclic by reversing some edges."
content_hash: 7229bf3a3818e22cb2f36b52bb8dc6a0a21bde26
last_modified_at: 2024-01-30
related_topics:
  - title: español version
    url: /es/common/acyclic.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/acyclic.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/acyclic.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/acyclic.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/acyclic.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/acyclic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# acyclic

Make a directed graph acyclic by reversing some edges.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://graphviz.org/pdf/acyclic.1.pdf>.

- Make a directed graph acyclic by reversing some edges:

`acyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Print if a graph is acyclic, has a cycle, or is undirected, producing no output graph:

`acyclic -v -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>

- Display help:

`acyclic -?`
