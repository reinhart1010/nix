---
layout: page
title: windows/get-acl (English)
description: "Get the security descriptor for a resource, such as a file or registry key."
content_hash: 12fa1bbfc21e24a52ca319a1f17e176f3943803b
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# Get-Acl

Get the security descriptor for a resource, such as a file or registry key.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl>.

- Display the ACL for a specific directory:

`Get-Acl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>

- Get an ACL for a registry key:

`Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HKLM:\System\CurrentControlSet\Control</span>` | Format-List`
