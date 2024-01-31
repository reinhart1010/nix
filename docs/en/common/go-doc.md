---
layout: page
title: common/go-doc (English)
description: "View documentation for a package or symbol."
content_hash: f411c0dfab34f70beaa4426af45007c58ede5c07
last_modified_at: 2024-01-31
related_topics:
  - title: Türkçe version
    url: /tr/common/go-doc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/go-doc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# go doc

View documentation for a package or symbol.
More information: <https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>.

- View documentation for the current package:

`go doc`

- Show package documentation and exported symbols:

`go doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- Show also documentation of symbols:

`go doc -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- Show also sources:

`go doc -all -src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- Show a specific symbol:

`go doc -all -src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json.Number</span>
