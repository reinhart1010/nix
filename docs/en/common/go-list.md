---
layout: page
title: common/go-list (English)
description: "List packages or modules."
content_hash: 1b359d0c158aae443c3b48a57368c72fb63d03f0
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/go-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go list

List packages or modules.
More information: <https://golang.org/cmd/go/#hdr-List_packages_or_modules>.

- List packages:

`go list ./...`

- List standard packages:

`go list std`

- List packages in JSON format:

`go list -json time net/http`

- List module dependencies and available updates:

`go list -m -u all`
