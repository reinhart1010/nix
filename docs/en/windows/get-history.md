---
layout: page
title: windows/get-history (English)
description: "Display PowerShell command history."
content_hash: 38e5d82dd8d4ce878a405726a046c4002217f50b
---
# Get-History

Display PowerShell command history.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-history>.

- Display the commands history list with ID:

`Get-History`

- Get PowerShell history item by ID:

`Get-History -Id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Display the last N commands:

`Get-History -Count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>
