---
layout: page
title: osx/pbcopy (English)
description: "Copy data from `stdin` to the clipboard."
content_hash: 7190a3c4582dcac0ae4a135675518d41b01e3065
last_modified_at: 2022-12-04
related_topics:
  - title: Indonesia version
    url: /id/osx/pbcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbcopy.html
    icon: bi bi-globe
---
# pbcopy

Copy data from `stdin` to the clipboard.
More information: <https://ss64.com/osx/pbcopy.html>.

- Place the contents of a specific file in the clipboard:

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Place the results of a specific command in the clipboard:

`find . -type t -name "*.png" | pbcopy`
