---
layout: page
title: common/zek (English)
description: "Generate a Go struct from XML."
content_hash: 13411905c6766a4d6dca261eff02732b8edc1c0d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# zek

Generate a Go struct from XML.
More information: <https://github.com/miku/zek>.

- Generate a Go struct from a given XML from `stdin` and display output on `stdout`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml</span>` | zek`

- Generate a Go struct from a given XML from `stdin` and send output to a file:

`curl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://url/to/xml</span>` | zek -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.go</span>

- Generate an example Go program from a given XML from `stdin` and send output to a file:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.xml</span>` | zek -p -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.go</span>
