---
layout: page
title: windows/resolve-path (English)
description: "Resolves the wildcard characters in a path, and displays the path contents."
content_hash: 224dda0afee328df440b727cf1d15319409db7d5
last_modified_at: 2022-12-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Resolve-Path

Resolves the wildcard characters in a path, and displays the path contents.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/resolve-path>.

- Resolve the home folder path:

`Resolve-Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~</span>

- Resolve a UNC path:

`Resolve-Path -Path "\\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`"`

- Get relative paths:

`Resolve-Path -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>` -Relative`
