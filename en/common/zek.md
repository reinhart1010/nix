---
layout: page
title: common/zek (English)
description: "Generate a Go struct from XML."
content_hash: fe33b649babe387720d991217df6c0c5f9e55e4f
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zek

Generate a Go struct from XML.
More information: <https://github.com/miku/zek>.

- Generate a Go struct from a given XML from stdin and display output on stdout:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml</span>` | zek`

- Generate a Go struct from a given XML from stdin and send output to a file:

`curl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://url/to/xml</span>` | zek -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.go</span>

- Generate an example Go program from a given XML from stdin and send output to a file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml</span>` | zek -p -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.go</span>
