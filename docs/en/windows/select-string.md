---
layout: page
title: windows/select-string (English)
description: "Finds text in strings and files in PowerShell."
content_hash: 70a07ff8ec9ba8f6c5a36b3f40073b56ad98bcd6
last_modified_at: 2022-12-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Select-String

Finds text in strings and files in PowerShell.
This command can only be used through PowerShell.
You can use `Select-String` similar to grep in UNIX or findstr.exe in Windows.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string>.

- Search for a pattern within a file:

`Select-String -Path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`" -Pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`'`

- Search for an exact string (disables regular expressions):

`Select-String -SimpleMatch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exact_string</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search for pattern in all `.ext` files in current dir:

`Select-String -Path "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`" -Pattern '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`'`

- Capture the specified number of lines before and after the line that matches the pattern:

`Select-String --Context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Search stdin for lines that do not match a pattern:

`Get-Content `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | Select-String --NotMatch "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_pattern</span>`"`
