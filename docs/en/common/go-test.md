---
layout: page
title: common/go-test (English)
description: "Tests Go packages (files have to end with `_test.go`)."
content_hash: a7301b18d04f10b44a20e92af4c8e930af5680d9
last_modified_at: 2024-11-04
related_topics:
  - title: 한국어 version
    url: /ko/common/go-test.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go-test.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go test

Tests Go packages (files have to end with `_test.go`).
More information: <https://pkg.go.dev/cmd/go#hdr-Testing_flags>.

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

- Test the package with coverage analysis:

`go test -cover`
