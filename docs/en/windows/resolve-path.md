---
layout: page
title: windows/resolve-path (English)
description: "Resolves the wildcard characters in a path, and displays the path contents."
content_hash: 997b8df4bb9a4ffd0574f390cc541ee886d559ea
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Resolve-Path

Resolves the wildcard characters in a path, and displays the path contents.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/resolve-path>.

- Resolve the home folder path:

`Resolve-Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~</span>

- Resolve a UNC path:

`Resolve-Path -Path "\\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>`"`

- Get relative paths:

`Resolve-Path -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file_or_directory</span>` -Relative`
