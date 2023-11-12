---
layout: page
title: common/gv2gxl (English)
description: "Convert a graph from `gv` to `gxl` format."
content_hash: dbe247075e6e9046e564550539d22c16d5a96d56
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gv2gxl

Convert a graph from `gv` to `gxl` format.
Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
More information: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- Convert a graph from `gv` to `gxl` format:

`gv2gxl -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gxl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gv</span>

- Convert a graph using `stdin` and `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gv</span>` | gv2gxl > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gxl</span>

- Display help:

`gv2gxl -?`
