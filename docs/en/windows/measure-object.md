---
layout: page
title: windows/measure-object (English)
description: "Calculates the numeric properties of objects, and the characters, words, and lines in string objects, such as files of text."
content_hash: 746399514e1d43a927d67d7e034f4a2c49c953df
last_modified_at: 2023-02-20
---
# Measure-Object

Calculates the numeric properties of objects, and the characters, words, and lines in string objects, such as files of text.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/measure-object>.

- Count the files and folders in a directory:

`Get-ChildItem | Measure-Object`

- Pipe input to Measure-Command (objects that are piped to `Measure-Command` are available to the script block that is passed to the Expression parameter):

`"One", "Two", "Three", "Four" | Set-Content -Path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>`"; Get-Content "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>`"; | Measure-Object -Character -Line -Word`
