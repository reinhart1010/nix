---
layout: page
title: common/go-test (English)
description: "Tests Go packages (files have to end with `_test.go`)."
content_hash: fe36d83144137f7744d4b7f3026b6fb179a87845
---
# go test

Tests Go packages (files have to end with `_test.go`).
More information: <https://golang.org/cmd/go/#hdr-Testing_flags>.

- Test the package found in the current directory:

`go test`

- [v]erbosely test the package in the current directory:

`go test -v`

- Test the packages in the current directory and all subdirectories (note the `...`):

`go test -v ./...`

- Test the package in the current directory and run all benchmarks:

`go test -v -bench .`

- Test the package in the current directory and run all benchmarks for 50 seconds:

`go test -v -bench . -benchtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50s</span>
