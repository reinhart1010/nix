---
layout: page
title: common/gml2gv (English)
description: "Convert a graph from `gml` to `gv` format."
content_hash: a95941fe6985d44e709d31dd99ba65fd3591f2e4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gml2gv

Convert a graph from `gml` to `gv` format.
Converters: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`.
More information: <https://graphviz.org/pdf/gml2gv.1.pdf>.

- Convert a graph from `gml` to `gv` format:

`gml2gv -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gml</span>

- Convert a graph using `stdin` and `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.gml</span>` | gml2gv > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.gv</span>

- Display help:

`gml2gv -?`
