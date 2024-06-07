---
layout: page
title: windows/get-acl (English)
description: "Get the security descriptor for a resource, such as a file or registry key."
content_hash: e771e0b5dc6b86d2ce4dcc03d94e0667e1ca6348
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Get-Acl

Get the security descriptor for a resource, such as a file or registry key.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl>.

- Display the ACL for a specific directory:

`Get-Acl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Get an ACL for a registry key:

`Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HKLM:\System\CurrentControlSet\Control</span>` | Format-List`
