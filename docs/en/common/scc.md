---
layout: page
title: common/scc (English)
description: "Tool written in Go that counts lines of code."
content_hash: 7d2386c8a13d6bd976ec58b8029d938ddf9e11e4
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/scc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scc

Tool written in Go that counts lines of code.
More information: <https://github.com/boyter/scc>.

- Print lines of code in the current directory:

`scc`

- Print lines of code in the target directory:

`scc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Display output for every file:

`scc --by-file`

- Display output using a specific output format (defaults to `tabular`):

`scc --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tabular|wide|json|csv|cloc-yaml|html|html-table</span>

- Only count files with specific file extensions:

`scc --include-ext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go, java, js</span>

- Exclude directories from being counted:

`scc --exclude-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.git,.hg</span>

- Display output and sort by column (defaults to by files):

`scc --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">files|name|lines|blanks|code|comments|complexity</span>

- Print help for scc:

`scc -h`
