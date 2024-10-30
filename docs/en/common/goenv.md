---
layout: page
title: common/goenv (English)
description: "Install, uninstall or switch between Golang versions."
content_hash: 7fa951832511d7506bcf743895db84362a7b1b4b
last_modified_at: 2024-10-30
tldri18n_status: 2
---
# goenv

Install, uninstall or switch between Golang versions.
Supports version numbers like "1.16.15" or "1.22.8" etc.
More information: <https://github.com/go-nv/goenv>.

- List all available goenv commands:

`goenv commands`

- Install a specific version of Golang:

`goenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go_version</span>

- Use a specific version of Golang in the current project:

`goenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go_version</span>

- Set the default Golang version:

`goenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go_version</span>

- List all available Golang versions and highlight the default one:

`goenv versions`

- Uninstall a given Go version:

`goenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go_version</span>

- Run an executable with the selected Go version:

`goenv exec go run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go_version</span>
