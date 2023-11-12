---
layout: page
title: common/go-install (English)
description: "Compile and install packages named by the import paths."
content_hash: 6b2d1e52b5062542608bcab4a50cd121c3094f1f
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/go-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go install

Compile and install packages named by the import paths.
More information: <https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies>.

- Compile and install the current package:

`go install`

- Compile and install a specific local package:

`go install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/package</span>

- Install the latest version of a program, ignoring `go.mod` in the current directory:

`go install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">golang.org/x/tools/gopls</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latest</span>

- Install a program at the version selected by `go.mod` in the current directory:

`go install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">golang.org/x/tools/gopls</span>
