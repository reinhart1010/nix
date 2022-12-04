---
layout: page
title: common/sd (English)
description: "Intuitive find & replace CLI."
content_hash: 0adce6b3d5a9be0db8c30d5e6df91b8233ce9608
last_modified_at: 2022-12-04
---
# sd

Intuitive find & replace CLI.
More information: <https://github.com/chmln/sd>.

- Trim some whitespace using a regular expression:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'lorem ipsum 23   '</span>` | sd '\s+$' ''`

- Replace words using capture groups:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'cargo +nightly watch'</span>` | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- Find and replace in a file printing the result to `stdout`:

`sd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'window.fetch'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'fetch'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http.js</span>

- Find and replace across a project changing each file in place:

`sd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'from "react"'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'from "preact"'</span>` $(find . -type f)`
