---
layout: page
title: windows/get-acl (English)
description: "Gets the security descriptor for a resource, such as a file or registry key."
content_hash: 6fe63e598013b3ca8af0a724b81f1a81f17b1f3e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Get-Acl

Gets the security descriptor for a resource, such as a file or registry key.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl>.

- Display the ACL for a specific directory:

`Get-Acl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Get an ACL for a registry key:

`Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HKLM:\System\CurrentControlSet\Control</span>` | Format-List`
