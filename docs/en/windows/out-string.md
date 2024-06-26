---
layout: page
title: windows/out-string (English)
description: "Outputs input objects as a string."
content_hash: 57e2c145a12fa69dbbd86e44651d31988ddc900c
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Out-String

Outputs input objects as a string.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/out-string>.

- Print host information as string:

`Get-Alias | Out-String`

- Convert each object to a string rather than concatenating all the objects into a single string:

`Get-Alias | Out-String -Stream`

- Use the `Width` parameter to prevent truncation:

`@{TestKey = ('x' * 200)} | Out-String -Width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">250</span>
