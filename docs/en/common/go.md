---
layout: page
title: common/go (English)
description: "Tool for managing go source code."
content_hash: 0ccb141dc6f3431b8261a2ba5412c74d9f21999c
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/go.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/go.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go

Tool for managing go source code.
Some subcommands such as `go build` have their own usage documentation.
More information: <https://golang.org>.

- Download and install a package, specified by its import path:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_path</span>

- Compile and run a source file (it has to contain a `main` package):

`go run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`.go`

- Compile a source file into a named executable:

`go build -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>`.go`

- Compile the package present in the current directory:

`go build`

- Execute all test cases of the current package (files have to end with `_test.go`):

`go test`

- Compile and install the current package:

`go install`

- Initialize a new module in the current directory:

`go mod init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>
