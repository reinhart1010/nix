---
layout: page
title: common/tred (English)
description: "Compute the transitive reduction of directed graphs."
content_hash: e75a26f8b0d643eea54beafb0847828028612bec
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/tred.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tred

Compute the transitive reduction of directed graphs.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://www.graphviz.org/pdf/tred.1.pdf>.

- Construct the transitive reduction graph of one or more directed graphs:

`tred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Display help:

`tred -?`
