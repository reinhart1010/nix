---
layout: page
title: common/gxl2gv (English)
description: "Convert a graph from `gxl` to `gv` format."
content_hash: 75233cb45fcb8c025682faace00dac41c03454f2
---
# gxl2gv

Convert a graph from `gxl` to `gv` format.
Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
More information: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- Convert a graph from `gxl` to `gv` format:

`gxl2gv -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gxl</span>

- Convert a graph using stdin and stdout:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gxl</span>` | gxl2gv > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>

- Display help:

`gxl2gv -?`
