---
layout: page
title: windows/get-alias (English)
description: "List and get command aliases in the current PowerShell session."
content_hash: 94f31bbe35554d9c65ecdd5d2c208d2d98b692df
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Get-Alias

List and get command aliases in the current PowerShell session.
This command can only be run under PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-alias>.

- List all aliases in the current session:

`Get-Alias`

- Get the aliased command name:

`Get-Alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_alias</span>

- List all aliases assigned to a specific command:

`Get-Alias -Definition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- List aliases that begins with `abc`, excluding those which ends at `def`:

`Get-Alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abc</span>`* -Exclude *`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">def</span>
