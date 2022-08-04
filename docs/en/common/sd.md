---
layout: page
title: common/sd (English)
description: "Intuitive find & replace CLI."
content_hash: bd41fb1cae5a438f154c2c52e22cb389fd4a3046
---
# sd

Intuitive find & replace CLI.
More information: <https://github.com/chmln/sd>.

- Trim some whitespace using a regular expression:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'lorem ipsum 23   '</span>` | sd '\s+$' ''`

- Replace words using capture groups:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'cargo +nightly watch'</span>` | sd '(\w+)\s+\+(\w+)\s+(\w+)' 'cmd: $1, channel: $2, subcmd: $3'`

- Find and replace in a file printing the result to stdout:

`sd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'window.fetch'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'fetch'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http.js</span>

- Find and replace across a project changing each file in place:

`sd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'from "react"'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'from "preact"'</span>` $(find . -type f)`
