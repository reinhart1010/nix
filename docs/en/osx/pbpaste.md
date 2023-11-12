---
layout: page
title: osx/pbpaste (English)
description: "Send the contents of the clipboard to `stdout`."
content_hash: 32aaed7f4bdab3b25e474302d76b25f5701b32d2
last_modified_at: 2023-11-12
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
More information: <https://ss64.com/osx/pbpaste.html>.

- Write the contents of the clipboard to a file:

`pbpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Use the contents of the clipboard as input to a command:

`pbpaste | grep foo`
