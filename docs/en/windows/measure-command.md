---
layout: page
title: windows/measure-command (English)
description: "Measures the time it takes to run script blocks and cmdlets."
content_hash: 3c2305de7fed1a8f6278acaa7a3d33217e6a34fd
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Measure-Command

Measures the time it takes to run script blocks and cmdlets.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-command>.

- Measure the time it takes to run a command:

`Measure-Command { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` }`

- Pipe input to Measure-Command (objects that are piped to `Measure-Command` are available to the script block that is passed to the Expression parameter):

`10, 20, 50 | Measure-Command -Expression { for ($i=0; $i -lt $_; $i++) {$i} }`
