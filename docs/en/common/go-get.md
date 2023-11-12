---
layout: page
title: common/go-get (English)
description: "Add a dependency package, or download packages in legacy GOPATH mode."
content_hash: 9c64c4fb4f727a86774eda7aa78d2666eedecfc8
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/go-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go get

Add a dependency package, or download packages in legacy GOPATH mode.
More information: <https://pkg.go.dev/cmd/go#hdr-Add_dependencies_to_current_module_and_install_them>.

- Add a specified package to `go.mod` in module-mode or install the package in GOPATH-mode:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/pkg</span>

- Modify the package with a given version in module-aware mode:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/pkg</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.2.3</span>

- Remove a specified package:

`go get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/pkg</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none</span>
