---
layout: page
title: common/go-env (English)
description: "Manage environment variables used by the Go toolchain."
content_hash: b5f7fa64b4a393d6afe8ffcc3ed9e5fc62b3e1f4
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/go-env.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-env.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go env

Manage environment variables used by the Go toolchain.
More information: <https://golang.org/cmd/go/#hdr-Print_Go_environment_information>.

- Show all environment variables:

`go env`

- Show a specific environment variable:

`go env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOPATH</span>

- Set an environment variable to a value:

`go env -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOBIN</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Reset an environment variable's value:

`go env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GOBIN</span>
