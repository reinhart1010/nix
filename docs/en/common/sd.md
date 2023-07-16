---
layout: page
title: common/sd (English)
description: "Intuitive find and replace."
content_hash: 4c73968008c77300e751b2f7de29e2b6fcb6f051
last_modified_at: 2023-07-16
---
# sd

Intuitive find and replace.
More information: <https://github.com/chmln/sd>.

- Trim some whitespace using a regular expression (output stream: `stdout`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'lorem ipsum 23   '</span>` | sd '\s+$' ''`

- Replace words using capture groups (output stream: `stdout`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'cargo +nightly watch'</span>` | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- Find and replace in a specific file (output stream: `stdout`):

`sd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'window.fetch'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'fetch'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.js</span>

- Find and replace in all files in the current project (output stream: `stdout`):

`sd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'from "react"'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'from "preact"'</span>` "$(find . -type f)"`
