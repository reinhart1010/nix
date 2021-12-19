---
layout: page
title: windows/clip (English)
description: "Copy input content to the Windows clipboard."
content_hash: 8c8250f8598608de6e76118bb7ed4f1cd7752a80
related_topics:
  - title: 日本語 version
    url: /ja/windows/clip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/clip.html
    icon: bi bi-globe
---
# clip

Copy input content to the Windows clipboard.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/clip>.

- Pipe command-line output to the Windows clipboard:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | clip`

- Copy the contents of a file to the Windows clipboard:

`clip < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ext</span>

- Copy text with a trailing newline to the Windows clipboard:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some text</span>` | clip`

- Copy text without a trailing newline to the Windows clipboard:

`echo | set /p="some text" | clip`
