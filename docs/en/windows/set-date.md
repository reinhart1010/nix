---
layout: page
title: windows/set-date (English)
description: "Changes the system time on the computer to a time that you specify."
content_hash: 8fd8ec6ff2139f3816f551051eb26450d7972698
last_modified_at: 2024-06-07
tldri18n_status: 2
---
# Set-Date

Changes the system time on the computer to a time that you specify.
Note: This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/set-date>.

- Add three days to the system date:

`Set-Date -Date (Get-Date).AddDays(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>`)`

- Set the system clock back 10 minutes:

`Set-Date -Adjust -0:10:0 -DisplayHint Time`

- Add 90 minutes to the system clock:

`$90mins = New-TimeSpan -Minutes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90</span>`; Set-Date -Adjust $90mins`
