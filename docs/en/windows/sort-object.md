---
layout: page
title: windows/sort-object (English)
description: "Sorts objects by property values."
content_hash: 67b9a434a86833c4ae2c17247761a3f1732cc4f6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Sort-Object

Sorts objects by property values.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/sort-object>.

- Sort the current directory by name:

`Get-ChildItem | Sort-Object`

- Sort the current directory by name descending:

`Get-ChildItem | Sort-Object -Descending`

- Sort items removing duplicates:

`"a", "b", "a" | Sort-Object -Unique`

- Sort the current directory by file length:

`Get-ChildItem | Sort-Object -Property Length`

- Sort processes with the highest memory usage based on their working set (WS) size:

`Get-Process | Sort-Object -Property WS`
