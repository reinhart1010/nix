---
layout: page
title: windows/get-help (English)
description: "Display help information and documentation for PowerShell commands, aka. cmdlets."
content_hash: efcd121f7c56e3dc19b19c1096e06925a34dd9d1
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Get-Help

Display help information and documentation for PowerShell commands, aka. cmdlets.
This command can only be run through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-help>.

- Display general help information for a specific cmdlet:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmdlet</span>

- Display a more detailed documentation for a specific cmdlet:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmdlet</span>` -Detailed`

- Display the full technical documentation for a specific cmdlet:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmdlet</span>` -Full`

- Print only the documentation for a specific parameter of the cmdlet (use `*` to show all parameters), if available:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmdlet</span>` -Parameter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parameter</span>

- Print only the examples of the cmdlet, if available:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmdlet</span>` -Examples`

- List all available cmdlet help pages:

`Get-Help *`

- Update the current help and documentation knowledge base using `Update-Help`:

`Update-Help`

- View an online version of cmdlet documentation in the default web browser:

`Get-Help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmdlet</span>` -Online`
