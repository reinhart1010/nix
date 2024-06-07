---
layout: page
title: windows/get-date (English)
description: "Get the current date and time."
content_hash: e71a1d9b31826eef0527c39eb4634d61f11dbee6
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Get-Date

Get the current date and time.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-date>.

- Display the current date and time:

`Get-Date`

- Display the current date and time with a .NET format specifier:

`Get-Date -Format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yyyy-MM-dd HH:mm:ss</span>`"`

- Display the current date and time in UTC and ISO 8601 format:

`(Get-Date).ToUniversalTime()`

- Convert a Unix timestamp:

`Get-Date -UnixTimeSeconds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1577836800</span>
