---
layout: page
title: common/gofmt (English)
description: "Format Go source code."
content_hash: 330a910832f0b821a877be90c2da4c0a320b96b9
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# gofmt

Format Go source code.
More information: <https://golang.org/cmd/gofmt/>.

- Format a file and display the result to the console:

`gofmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>

- Format a file, overwriting the original file in-place:

`gofmt -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>

- Format a file, and then simplify the code, overwriting the original file:

`gofmt -s -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>

- Print all (including spurious) errors:

`gofmt -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.go</span>
