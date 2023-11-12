---
layout: page
title: common/go-build (English)
description: "Compile Go sources."
content_hash: 6af81b12fdc4701965abcbf109f9a64e7387d52d
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/go-build.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go build

Compile Go sources.
More information: <https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>.

- Compile a 'package main' file (output will be the filename without extension):

`go build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/main.go</span>

- Compile, specifying the output filename:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source.go</span>

- Compile a package:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/binary</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package</span>

- Compile a main package into an executable, enabling data race detection:

`go build -race -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/main/package</span>
