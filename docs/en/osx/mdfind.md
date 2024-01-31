---
layout: page
title: osx/mdfind (English)
description: "List files matching a given query."
content_hash: bdacdf440b4b44cf72a7454414aa37ead1fbd80e
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/mdfind.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/mdfind.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mdfind

List files matching a given query.
More information: <https://keith.github.io/xcode-man-pages/mdfind.1.html>.

- Find a file by its name:

`mdfind -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Find a file by its content:

`mdfind "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`

- Find a file containing a string, in a given directory:

`mdfind -onlyin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`
