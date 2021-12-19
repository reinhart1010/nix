---
layout: page
title: windows/get-history (English)
description: "Display PowerShell command history."
content_hash: cd697ec43d64dd1ab2d7f5c44b9eff381dd469a6
---
# Get-History

Display PowerShell command history.
This command can only be used through PowerShell.
More information: <https://docs.microsoft.com/powershell/module/microsoft.powershell.core/get-history>.

- Display the commands history list with ID:

`Get-History`

- Get PowerShell history item by ID:

`Get-History -Id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- Display the last N commands:

`Get-History -Count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>
