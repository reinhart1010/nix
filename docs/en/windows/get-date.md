---
layout: page
title: windows/get-date (English)
description: "Gets the current date and time."
content_hash: dbc7937704dcbb9e53ed7643eae5c50b1411779b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Get-Date

Gets the current date and time.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-date>.

- Display the current date and time:

`Get-Date`

- Display the current date and time with a .NET format specifier:

`Get-Date -Format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yyyy-MM-dd HH:mm:ss</span>`"`

- Display the current date and time in UTC and ISO 8601 format:

`(Get-Date).ToUniversalTime()`

- Convert a Unix timestamp:

`Get-Date -UnixTimeSeconds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1577836800</span>
