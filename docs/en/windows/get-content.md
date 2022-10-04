---
layout: page
title: windows/get-content (English)
description: "Get the content of the item at the specified location."
content_hash: a6de0171d626a0e35d016f25e7ad2ce8900da921
---
# Get-Content

Get the content of the item at the specified location.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- Display the content of a file:

`Get-Content -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display the first few lines of a file:

`Get-Content -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -TotalCount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>

- Display the content of the file and keep reading from it until `Ctrl + C` is pressed:

`Get-Content -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -Wait`
