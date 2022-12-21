---
layout: page
title: windows/get-acl (English)
description: "Gets the security descriptor for a resource, such as a file or registry key."
content_hash: 572508c47ac352372d9c46ccd7fe4b9909ba8842
last_modified_at: 2022-12-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Get-Acl

Gets the security descriptor for a resource, such as a file or registry key.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/get-acl>.

- Display the ACL for a specific directory:

`Get-Acl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Get an ACL for a registry key:

`Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HKLM:\System\CurrentControlSet\Control</span>` | Format-List`
