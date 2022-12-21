---
layout: page
title: windows/set-acl (English)
description: "Changes the security descriptor of a specified item, such as a file or a registry key."
content_hash: 407a343c5a272b8e9fe841ecacf7e53d35fd2a7a
last_modified_at: 2022-12-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Set-Acl

Changes the security descriptor of a specified item, such as a file or a registry key.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.security/set-acl>.

- Copy a security descriptor from one file to another:

`$OriginAcl = Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`; Set-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -AclObject $OriginAcl`

- Use the pipeline operator to pass a descriptor:

`Get-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | Set-Acl -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
