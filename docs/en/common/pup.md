---
layout: page
title: common/pup (English)
description: "Command-line HTML parsing tool."
content_hash: e70cc14ab06b51c6be5e8a7f89347d89ca7849e9
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# pup

Command-line HTML parsing tool.
More information: <https://github.com/ericchiang/pup>.

- Transform a raw HTML file into a cleaned, indented, and colored format:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup --color`

- Filter HTML by element tag name:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>`'`

- Filter HTML by ID:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">div#id</span>`'`

- Filter HTML by attribute value:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input[type="text"]</span>`'`

- Print all text from the filtered HTML elements and their children:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">div</span>` text{}'`

- Print HTML as JSON:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index.html</span>` | pup '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">div</span>` json{}'`
