---
layout: page
title: windows/forfiles (English)
description: "Select files to execute a specified command on."
content_hash: 7afddde4d88420e9f87da6f9d2f47950cdbe07f8
last_modified_at: 2024-01-25
related_topics:
  - title: 中文 version
    url: /zh/windows/forfiles.html
    icon: bi bi-globe
tldri18n_status: 2
---
# forfiles

Select files to execute a specified command on.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/forfiles>.

- Search for files in the current directory:

`forfiles`

- Search for files in a specific directory:

`forfiles /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Run the specified command for each file:

`forfiles /c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Search for files using a specific glob mask:

`forfiles /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">glob_pattern</span>

- Search for files recursively:

`forfiles /s`

- Search for files older than 5 days:

`forfiles /d +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
