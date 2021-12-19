---
layout: page
title: common/gox (English)
description: "A tool for cross-compiling Go programs."
content_hash: 4ea10e809aa24be4d7ead5c3cadcf8c0697ec8fc
---
# gox

A tool for cross-compiling Go programs.
More information: <https://github.com/mitchellh/gox>.

- Compile Go program in the current directory for all operating systems and architecture combinations:

`gox`

- Download and compile a Go program from a remote URL:

`gox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_2</span>

- Compile current directory for a particular operating system:

`gox -os="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>`"`

- Compile current directory for a single operating system and architecture combination:

`gox -osarch="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">os</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arch</span>`"`
