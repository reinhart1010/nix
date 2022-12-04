---
layout: page
title: common/mm2gv (English)
description: "Convert a graph from Matrix Market `mm` format to `gv` format."
content_hash: 8b3ba52b1bd279f68fd881bfa444ff1a29719af6
last_modified_at: 2022-12-04
---
# mm2gv

Convert a graph from Matrix Market `mm` format to `gv` format.
Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
More information: <https://graphviz.org/pdf/mm2gv.1.pdf>.

- Convert a graph from `mm` to `gv` format:

`mm2gv -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mm</span>

- Convert a graph using `stdin` and `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.mm</span>` | mm2gv > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>

- Display help:

`mm2gv -?`
