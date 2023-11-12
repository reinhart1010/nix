---
layout: page
title: common/dot (English)
description: "Render an image of a `linear directed` network graph from a `graphviz` file."
content_hash: 097949fef76ba42cc6a97a15bf511b5d866989ea
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/dot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dot

Render an image of a `linear directed` network graph from a `graphviz` file.
Layouts: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` & `patchwork`.
More information: <https://graphviz.org/doc/info/command.html>.

- Render a `png` image with a filename based on the input filename and output format (uppercase -O):

`dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>

- Render a `svg` image with the specified output filename (lowercase -o):

`dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>

- Render the output in `ps`, `pdf`, `svg`, `fig`, `png`, `gif`, `jpg`, `json`, or `dot` format:

`dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.gv</span>

- Render a `gif` image using `stdin` and `stdout`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">digraph {this -> that} </span>`" | dot -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gif</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.gif</span>

- Display help:

`dot -?`
