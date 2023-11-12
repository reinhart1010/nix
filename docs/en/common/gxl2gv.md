---
layout: page
title: common/gxl2gv (English)
description: "Convert a graph from `gxl` to `gv` format."
content_hash: dd602247c5b4946a02c8c95382dced06e6edacbe
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gxl2gv

Convert a graph from `gxl` to `gv` format.
Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
More information: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- Convert a graph from `gxl` to `gv` format:

`gxl2gv -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gxl</span>

- Convert a graph using `stdin` and `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gxl</span>` | gxl2gv > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>

- Display help:

`gxl2gv -?`
