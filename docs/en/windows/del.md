---
layout: page
title: windows/del (English)
description: "Delete one or more files."
content_hash: eda6f28eee95d0d14f6d89fb57956d2eaaeee809
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/del.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/del.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/del.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/del.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/del.html
    icon: bi bi-globe
tldri18n_status: 2
---
# del

Delete one or more files.
In PowerShell, this command is an alias of `Remove-Item`. This documentation is based on the Command Prompt (`cmd`) version of `del`.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- View the documentation of the equivalent PowerShell command:

`tldr remove-item`

- Delete one or more space-separated files or patterns:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>

- Prompt for confirmation before deleting each file:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /p`

- Force the deletion of read-only files:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /f`

- Recursively delete file(s) from all subdirectories:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /s`

- Do not prompt when deleting files based on a global wildcard:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /q`

- Display the help and list available attributes:

`del /?`

- Delete files based on specified attributes:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attribute</span>
