---
layout: page
title: windows/clip (English)
description: "Copy input content to the Windows clipboard."
content_hash: 0a1c1b91fd137774e9216529c3eff300da78c52f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/clip.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/clip.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/clip.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/clip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/clip.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/clip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clip

Copy input content to the Windows clipboard.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- Pipe command-line output to the Windows clipboard:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | clip`

- Copy the contents of a file to the Windows clipboard:

`clip < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file.ext</span>

- Copy text with a trailing newline to the Windows clipboard:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">some text</span>` | clip`

- Copy text without a trailing newline to the Windows clipboard:

`echo | set /p="some text" | clip`
