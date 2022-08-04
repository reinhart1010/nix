---
layout: page
title: common/go-doc (English)
description: "Show documentation for a package or symbol."
content_hash: 83d28cae326b904a97ddcbdf98e68159b6d7137f
---
# go doc

Show documentation for a package or symbol.
More information: <https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>.

- Show documentation for the current package:

`go doc`

- Show package documentation and exported symbols:

`go doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- Show also documentation of symbols:

`go doc -all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- Show also sources:

`go doc -all -src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json</span>

- Show a specific symbol:

`go doc -all -src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding/json.Number</span>
