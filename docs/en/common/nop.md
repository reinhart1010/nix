---
layout: page
title: common/nop (English)
description: "Check validity and pretty-print graphs in canonical format."
content_hash: dfdc696cd5e4da99c1940dea0df1c6fa1874f774
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/nop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nop

Check validity and pretty-print graphs in canonical format.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://www.graphviz.org/pdf/nop.1.pdf>.

- Pretty-print one or more graphs in canonical format:

`nop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Check one or more graphs for validity, producing no output graph:

`nop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>

- Display help for `nop`:

`nop -?`
