---
layout: page
title: windows/tee-object (English)
description: "Saves command output in a file or variable and also sends it down the pipeline."
content_hash: 6c10936bd4d1181136171d1bd8641d30f11160c5
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Tee-Object

Saves command output in a file or variable and also sends it down the pipeline.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/tee-object>.

- Output processes to a file and to the console:

`Get-Process | Tee-Object -FilePath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Output processes to a variable and `Select-Object`:

`Get-Process notepad | Tee-Object -Variable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proc</span>` | Select-Object processname,handles`
