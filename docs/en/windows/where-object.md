---
layout: page
title: windows/where-object (English)
description: "Selects objects from a collection based on their property values."
content_hash: bf5bcdc18341f1e2a23b4b3613dcf16b51821e69
last_modified_at: 2024-01-31
related_topics:
  - title: Nederlands version
    url: /nl/windows/where-object.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Where-Object

Selects objects from a collection based on their property values.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/where-object>.

- Filter aliases by its name:

`Get-Alias | Where-Object -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Property</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Name</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eq</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List all services that are currently stopped. The `$_` automatic variable represents each object that is passed to the `Where-Object` cmdlet:

`Get-Service | Where-Object {$_.Status -eq "Stopped"}`

- Use multiple conditions:

`Get-Module -ListAvailable | Where-Object { $_.Name -NotLike "Microsoft*" -And $_.Name -NotLike "PS*" }`
