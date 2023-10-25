---
layout: page
title: windows/rmdir (English)
description: "Remove a directory and its contents."
content_hash: 36d3f5e93b47be8f115683864445fe75900d2aa9
last_modified_at: 2023-10-25
related_topics:
  - title: Nederlands version
    url: /nl/windows/rmdir.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/rmdir.html
    icon: bi bi-globe
---
# rmdir

Remove a directory and its contents.
In PowerShell, this command is an alias of `Remove-Item`. This documentation is based on the Command Prompt (`cmd`) version of `rmdir`.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- View the documentation of the equivalent PowerShell command:

`tldr remove-item`

- Remove an empty directory:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Remove a directory and its contents recursively:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` /s`

- Remove a directory and its contents recursively without prompting:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` /s /q`
