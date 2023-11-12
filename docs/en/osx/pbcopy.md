---
layout: page
title: osx/pbcopy (English)
description: "Copy data from `stdin` to the clipboard."
content_hash: 2811b12339ce628f1eb25677af749c70c5562cf7
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/pbcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbcopy.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/pbcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbcopy

Copy data from `stdin` to the clipboard.
Comparable to pressing Cmd + C on the keyboard.
More information: <https://ss64.com/osx/pbcopy.html>.

- Place the contents of a specific file in the clipboard:

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Place the results of a specific command in the clipboard:

`find . -type t -name "*.png" | pbcopy`
