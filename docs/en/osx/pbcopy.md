---
layout: page
title: osx/pbcopy (English)
description: "Copy data from stdin to the clipboard."
content_hash: c94828514c3799b78cb5dda3c398ad02bf4a46f7
related_topics:
  - title: Indonesia version
    url: /id/osx/pbcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbcopy.html
    icon: bi bi-globe
---
# pbcopy

Copy data from stdin to the clipboard.
More information: <https://ss64.com/osx/pbcopy.html>.

- Place the contents of a specific file in the clipboard:

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Place the results of a specific command in the clipboard:

`find . -type t -name "*.png" | pbcopy`
