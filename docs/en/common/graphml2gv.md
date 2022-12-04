---
layout: page
title: common/graphml2gv (English)
description: "Convert a graph from `graphml` to `gv` format."
content_hash: 062f5eec903e4a0ae5d37f7db876fb30706f9c75
last_modified_at: 2022-12-04
---
# graphml2gv

Convert a graph from `graphml` to `gv` format.
Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
More information: <https://graphviz.org/pdf/graphml2gv.1.pdf>.

- Convert a graph from `gml` to `gv` format:

`graphml2gv -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gml</span>

- Convert a graph using `stdin` and `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gml</span>` | graphml2gv > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>

- Display help:

`graphml2gv -?`
