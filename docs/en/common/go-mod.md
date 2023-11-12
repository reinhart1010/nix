---
layout: page
title: common/go-mod (English)
description: "Module maintenance."
content_hash: 1b74283f6baba7b0f90e0b88ae1f421674b69774
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/go-mod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go mod

Module maintenance.
More information: <https://golang.org/cmd/go/#hdr-Module_maintenance>.

- Initialize new module in current directory:

`go mod init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">moduleName</span>

- Download modules to local cache:

`go mod download`

- Add missing and remove unused modules:

`go mod tidy`

- Verify dependencies have expected content:

`go mod verify`

- Copy sources of all dependencies into the vendor directory:

`go mod vendor`
