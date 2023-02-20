---
layout: page
title: windows/wsl-open (English)
description: "Open a file or URL from within Windows Subsystem for Linux in the user's default Windows GUI application."
content_hash: 7da629d71db0b0c990ba14eb7c6fc3e2d90174e1
last_modified_at: 2023-02-20
---
# wsl-open

Open a file or URL from within Windows Subsystem for Linux in the user's default Windows GUI application.
More information: <https://gitlab.com/4U6U57/wsl-open>.

- Open the current directory in Windows Explorer:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Open a URL in the user's default web browser in Windows:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Open a specific file in the user's default application in Windows:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Set `wsl-open` as the shell's web browser (open links with `wsl-open`):

`wsl-open -w`

- Display help:

`wsl-open -h`
