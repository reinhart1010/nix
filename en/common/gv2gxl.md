---
layout: page
title: common/gv2gxl (English)
description: "Convert a graph from `gv` to `gxl` format."
content_hash: c0a66f20529133de57daa57da4d1d9441f282510
---
# gv2gxl

Convert a graph from `gv` to `gxl` format.
Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
More information: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- Convert a graph from `gv` to `gxl` format:

`gv2gxl -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gxl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gv</span>

- Convert a graph using stdin and stdout:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gv</span>` | gv2gxl > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gxl</span>

- Display help:

`gv2gxl -?`
