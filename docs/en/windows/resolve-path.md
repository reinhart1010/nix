---
layout: page
title: windows/resolve-path (English)
description: "Resolves the wildcard characters in a path, and displays the path contents."
content_hash: 4077957fb39228a728134809beff6ef570c9b442
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Resolve-Path

Resolves the wildcard characters in a path, and displays the path contents.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/resolve-path>.

- Resolve the home folder path:

`Resolve-Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~</span>

- Resolve a UNC path:

`Resolve-Path -Path "\\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>`"`

- Get relative paths:

`Resolve-Path -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` -Relative`
