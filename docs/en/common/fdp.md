---
layout: page
title: common/fdp (English)
description: "Render an image of a `force-directed` network graph from a `graphviz` file."
content_hash: e925733f190ff3ce6130b7d217983638b9860e5a
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/fdp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdp

Render an image of a `force-directed` network graph from a `graphviz` file.
Layouts: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`.
More information: <https://graphviz.org/doc/info/command.html>.

- Render a `png` image with a filename based on the input filename and output format (uppercase -O):

`fdp -T png -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>

- Render a `svg` image with the specified output filename (lowercase -o):

`fdp -T svg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>

- Render the output in a specific format:

`fdp -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps|pdf|svg|fig|png|gif|jpg|json|dot</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>

- Render a `gif` image using `stdin` and `stdout`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">digraph {this -> that} </span>`" | fdp -T gif > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.gif</span>

- Display help:

`fdp -?`
