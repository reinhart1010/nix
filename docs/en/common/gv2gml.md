---
layout: page
title: common/gv2gml (English)
description: "Convert a graph from `gv` to `gml` format."
content_hash: 36dcd7fa1e652803b085cca2b8e36581363a4c76
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gv2gml

Convert a graph from `gv` to `gml` format.
Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
More information: <https://graphviz.org/pdf/gml2gv.1.pdf>.

- Convert a graph from `gv` to `gml` format:

`gv2gml -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gv</span>

- Convert a graph using `stdin` and `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gv</span>` | gv2gml > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gml</span>

- Display help:

`gv2gml -?`
