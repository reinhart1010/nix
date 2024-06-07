---
layout: page
title: windows/get-history (English)
description: "Display PowerShell command history."
content_hash: 06cebdf036f9f3f1bc5e65d0830fa8795e1b64ef
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Get-History

Display PowerShell command history.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-history>.

- Display the commands history list with ID:

`Get-History`

- Get PowerShell history item by ID:

`Get-History -Id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Display the last N commands:

`Get-History -Count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
