---
layout: page
title: windows/get-childitem (English)
description: "List items in a directory."
content_hash: 6d92c1a397056a175b5779f829f93a8bc99e18a7
last_modified_at: 2023-11-12
tldri18n_status: 2
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

`Get-ChildItem -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>
