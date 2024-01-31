---
layout: page
title: osx/pbpaste (English)
description: "Send the contents of the clipboard to `stdout`."
content_hash: 0f3ba36a27fd3324f303efd21cd2b1b35cd2b144
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/pbpaste.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/pbpaste.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbpaste.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/pbpaste.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbpaste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbpaste

Send the contents of the clipboard to `stdout`.
Comparable to pressing Cmd + V on the keyboard.
More information: <https://keith.github.io/xcode-man-pages/pbpaste.1.html>.

- Write the contents of the clipboard to a file:

`pbpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use the contents of the clipboard as input to a command:

`pbpaste | grep foo`
