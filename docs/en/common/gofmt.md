---
layout: page
title: common/gofmt (English)
description: "Tool for formatting Go source code."
content_hash: 0fdc1986567334b3c643c1af597d05760e358933
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# gofmt

Tool for formatting Go source code.
More information: <https://golang.org/cmd/gofmt/>.

- Format a file and display the result to the console:

`gofmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>

- Format a file, overwriting the original file in-place:

`gofmt -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>

- Format a file, and then simplify the code, overwriting the original file:

`gofmt -s -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>

- Print all (including spurious) errors:

`gofmt -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>
