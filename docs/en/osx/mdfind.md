---
layout: page
title: osx/mdfind (English)
description: "List files matching a query."
content_hash: 64a46a0c4103b7318d24dc5f82b8eb27089aed4a
last_modified_at: 2024-02-15
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

List files matching a query.
More information: <https://keith.github.io/xcode-man-pages/mdfind.1.html>.

- Find a file by its name:

`mdfind -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Find a file by its content:

`mdfind "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`

- Find a file containing a string, in a given directory:

`mdfind -onlyin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`
