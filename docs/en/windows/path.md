---
layout: page
title: windows/path (English)
description: "Display or set the search path for executable files."
content_hash: afdb2360c8c945ffd80aa961a55956479920027e
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/path.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/path.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/path.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/path.html
    icon: bi bi-globe
tldri18n_status: 2
---
# path

Display or set the search path for executable files.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/path>.

- Display the current path:

`path`

- Set the path to one or more semicolon-separated directories:

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory1 path\to\directory2 ...</span>

- Append a new directory to the original path:

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>`;%path%`

- Set command prompt to only search the current directory for executables:

`path ;`
