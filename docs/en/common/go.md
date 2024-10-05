---
layout: page
title: common/go (English)
description: "Manage Go source code."
content_hash: 85f6c7338e582a3d04697b2f6e0ec3524f69b6bf
last_modified_at: 2024-10-05
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

Manage Go source code.
Some subcommands such as `build` have their own usage documentation.
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
