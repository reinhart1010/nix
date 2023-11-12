---
layout: page
title: osx/mdfind (English)
description: "List files matching a given query."
content_hash: bac0526804ed7b391dd95bf52d295f1ee18e3a03
last_modified_at: 2023-11-12
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
More information: <https://ss64.com/osx/mdfind.html>.

- Find a file by its name:

`mdfind -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Find a file by its content:

`mdfind "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`

- Find a file containing a string, in a given directory:

`mdfind -onlyin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">query</span>`"`
