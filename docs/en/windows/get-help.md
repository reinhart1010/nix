---
layout: page
title: windows/get-help (English)
description: "Display help information and documentation for PowerShell commands (aliases, cmdlets, and functions)."
content_hash: 2c238be31ca2ec9399b40012c34d0f0fce2a85ac
last_modified_at: 2023-11-30
tldri18n_status: 2
---
# Get-Help

Display help information and documentation for PowerShell commands (aliases, cmdlets, and functions).
This command can only be run through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-help>.

- Display general help information for a specific PowerShell command:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display a more detailed documentation for a specific PowerShell command:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -Detailed`

- Display the full technical documentation for a specific PowerShell command:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -Full`

- Print only the documentation for a specific parameter of the PowerShell command (use `*` to show all parameters), if available:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -Parameter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parameter</span>

- Print only the examples of the cmdlet, if available:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -Examples`

- List all available cmdlet help pages:

`Get-Help *`

- Update the current help and documentation knowledge base using `Update-Help`:

`Update-Help`

- View an online version of PowerShell command documentation in the default web browser:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` -Online`
