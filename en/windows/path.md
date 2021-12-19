---
layout: page
title: windows/path (English)
description: "Display or set the search path for executable files."
content_hash: 46b7875a4461e7e644b7e74d9869eea870fec1d7
related_topics:
  - title: 中文 version
    url: /zh/windows/path.html
    icon: bi bi-globe
---
# path

Display or set the search path for executable files.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/path>.

- Display the current path:

`path`

- Set the path to one or more semicolon-separated directories:

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory(s)</span>

- Append a new directory to the original path:

`path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>`;%path%`

- Set command prompt to only search the current directory for executables:

`path ;`
