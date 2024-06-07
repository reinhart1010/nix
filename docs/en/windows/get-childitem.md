---
layout: page
title: windows/get-childitem (English)
description: "List items in a directory."
content_hash: 35dcf75426e920435d81d7f6d7ebf297c4a52dc1
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Get-ChildItem

List items in a directory.
Note: This command can only be used through PowerShell.
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

`Get-ChildItem -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>
