---
layout: page
title: windows/del (English)
description: "Delete one or more files."
content_hash: dd63b4cc751a32e2c725caa48d4bd4342c9e6c29
related_topics:
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
---
# del

Delete one or more files.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/del>.

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
