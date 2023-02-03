---
layout: page
title: osx/pbpaste (English)
description: "Send the contents of the clipboard to standard output."
content_hash: 43e8d97b6df9141fdccf9261fb1f1e547899e7e5
last_modified_at: 2023-02-03
related_topics:
  - title: Deutsch version
    url: /de/osx/pbpaste.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbpaste.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbpaste.html
    icon: bi bi-globe
---
# pbpaste

Send the contents of the clipboard to standard output.
Comparable to pressing Cmd + V on the keyboard.
More information: <https://ss64.com/osx/pbpaste.html>.

- Write the contents of the clipboard to a file:

`pbpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use the contents of the clipboard as input to a command:

`pbpaste | grep foo`
