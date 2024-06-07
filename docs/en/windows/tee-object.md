---
layout: page
title: windows/tee-object (English)
description: "Saves command output in a file or variable and also sends it down the pipeline."
content_hash: 1eddcdc07af2df4bf2ec440a09fcf70e8821a957
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Tee-Object

Saves command output in a file or variable and also sends it down the pipeline.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/tee-object>.

- Output processes to a file and to the console:

`Get-Process | Tee-Object -FilePath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Output processes to a variable and `Select-Object`:

`Get-Process notepad | Tee-Object -Variable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proc</span>` | Select-Object processname,handles`
