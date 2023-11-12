---
layout: page
title: common/go-fmt (English)
description: "Format Go source files."
content_hash: ec3e8384c57d300c2033fac75e99c71e07b5e236
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/go-fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go fmt

Format Go source files.
Prints the filenames that are changed.
More information: <https://pkg.go.dev/cmd/go#hdr-Gofmt__reformat__package_sources>.

- Format Go source files in the current directory:

`go fmt`

- Format a specific Go package in your import path (`$GOPATH/src`):

`go fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package</span>

- Format the package in the current directory and all subdirectories (note the `...`):

`go fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./...</span>

- Print what format commands would've been run, without modifying anything:

`go fmt -n`

- Print which format commands are run as they are run:

`go fmt -x`
