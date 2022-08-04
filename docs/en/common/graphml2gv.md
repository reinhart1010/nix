---
layout: page
title: common/graphml2gv (English)
description: "Convert a graph from `graphml` to `gv` format."
content_hash: a73a3b0f14ab74300f7873a182cf8c1c56956e50
---
# graphml2gv

Convert a graph from `graphml` to `gv` format.
Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
More information: <https://graphviz.org/pdf/graphml2gv.1.pdf>.

- Convert a graph from `gml` to `gv` format:

`graphml2gv -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gml</span>

- Convert a graph using stdin and stdout:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gml</span>` | graphml2gv > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>

- Display help:

`graphml2gv -?`
