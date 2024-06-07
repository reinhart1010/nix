---
layout: page
title: windows/set-acl (English)
description: "Changes the security descriptor of a specified item, such as a file or a registry key."
content_hash: 7b400691ff2e4351cedc9e0034355267787710b7
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Set-Acl

Changes the security descriptor of a specified item, such as a file or a registry key.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-acl>.

- Copy a security descriptor from one file to another:

`$OriginAcl = Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>`; Set-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` -AclObject $OriginAcl`

- Use the pipeline operator to pass a descriptor:

`Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` | Set-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>
