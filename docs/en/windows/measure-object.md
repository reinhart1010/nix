---
layout: page
title: windows/measure-object (English)
description: "Calculates the numeric properties of objects, and the characters, words, and lines in string objects, such as files of text."
content_hash: 6068d3c0a8c9988482478edce52f837b807c0dc2
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Measure-Object

Calculates the numeric properties of objects, and the characters, words, and lines in string objects, such as files of text.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-object>.

- Count the files and folders in a directory:

`Get-ChildItem | Measure-Object`

- Pipe input to Measure-Command (objects that are piped to `Measure-Command` are available to the script block that is passed to the Expression parameter):

`"One", "Two", "Three", "Four" | Set-Content -Path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>`"; Get-Content "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>`"; | Measure-Object -Character -Line -Word`
