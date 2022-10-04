---
layout: page
title: windows/get-childitem (English)
description: "List items in a directory."
content_hash: 6abdb66c581bf4778f90296e5c0347c0e4c06a89
---
# Get-ChildItem

List items in a directory.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-childitem>.

- List all non-hidden items in the current directory:

`Get-ChildItem`

- List only directories in the current directory:

`Get-ChildItem -Directory`

- List only files in the current directory:

`Get-ChildItem -File`

- List items in the current directory, including hidden items:

`Get-ChildItem -Hidden`

- List items in a directory other than the current one:

`Get-ChildItem -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
