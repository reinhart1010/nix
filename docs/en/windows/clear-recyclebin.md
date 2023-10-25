---
layout: page
title: windows/clear-recyclebin (English)
description: "Clear items from the Recycle Bin."
content_hash: bb921cbca21c41cdfee1366241f2f75559676cc5
last_modified_at: 2023-10-25
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Clear-RecycleBin

Clear items from the Recycle Bin.
This command can only be used through PowerShell versions 5.1 and below, or 7.1 and above.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/clear-recyclebin>.

- Clear and delete all items inside the Recycle Bin:

`Clear-RecycleBin`

- Clear the Recycle Bin for a specific drive:

`Clear-RecycleBin -DriveLetter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>

- Clear the Recycle Bin without further confirmation:

`Clear-RecycleBin -Force`
