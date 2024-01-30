---
layout: page
title: common/unflatten (English)
description: "Adjust directed graphs to improve the layout aspect ratio."
content_hash: 90db8207c553422dcf807dc0d6c4675e48e0e664
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/common/unflatten.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unflatten

Adjust directed graphs to improve the layout aspect ratio.
Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
More information: <https://www.graphviz.org/pdf/unflatten.1.pdf>.

- Adjust one or more directed graphs to improve the layout aspect ratio:

`unflatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input1.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input2.gv ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gv</span>

- Use `unflatten` as a preprocessor for `dot` layout to improve aspect ratio:

`unflatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>` | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.png</span>

- Display help:

`unflatten -?`
