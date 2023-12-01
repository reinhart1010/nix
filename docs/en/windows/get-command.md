---
layout: page
title: windows/get-command (English)
description: "List and get available commands in the current PowerShell session."
content_hash: b040dcbc81fbc2d3d8be3a2cd6df9dceccd5e3d0
last_modified_at: 2023-12-01
tldri18n_status: 2
---
# Get-Command

List and get available commands in the current PowerShell session.
This command can only be run through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-command>.

- List all available PowerShell commands (aliases, cmdlets, functions) in the current computer:

`Get-Command`

- List all available PowerShell commands in the current session:

`Get-Command -ListImported`

- List only PowerShell aliases/cmdlets/functions available in the computer:

`Get-Command -Type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Alias|Cmdlet|Function</span>

- List only programs or commands available on PATH in the current session:

`Get-Command -Type Application`

- List only PowerShell commands by the module name, e.g. `Microsoft.PowerShell.Utility` for utility-related commands:

`Get-Command -Module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module</span>

- Get the command information (e.g. version number or module name) by its name:

`Get-Command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
