---
layout: page
title: common/zipgrep (English)
description: "Find patterns in files in a ZIP archive using extended regular expression (supports `?`, `+`, `{}`, `()` and `|`)."
content_hash: 5053037e367453872ce61d0ec9031e8fa58cb5e7
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# zipgrep

Find patterns in files in a ZIP archive using extended regular expression (supports `?`, `+`, `{}`, `()` and `|`).
More information: <https://manned.org/zipgrep>.

- Search for a pattern within a ZIP archive:

`zipgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Print file name and line number for each match:

`zipgrep -H -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Search for lines that do not match a pattern:

`zipgrep -v "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>

- Specify files inside a ZIP archive from search:

`zipgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file/to/search1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file/to/search2</span>

- Exclude files inside a ZIP archive from search:

`zipgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.zip</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file/to/exclude1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file/to/exclude2</span>
