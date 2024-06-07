---
layout: page
title: windows/invoke-item (English)
description: "Open files in their respective default programs."
content_hash: fe32301e855446e9ddb06ab4e0726d79e3c7c212
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Invoke-Item

Open files in their respective default programs.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/invoke-item>.

- Open a file in its default program:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Open all files inside a directory:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>`\*`

- Open all PNGs inside a directory:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>`\*.png`

- Open all files inside a directory containing a specific keyword:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>`\* -Include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*keyword*</span>

- Open all files inside a directory except those containing a specific keyword:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>`\* -Exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*keyword*</span>

- Perform a dry run to determine which files will be opened inside a directory through `Invoke-Item`:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>`\* -WhatIf`
