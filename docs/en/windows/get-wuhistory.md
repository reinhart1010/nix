---
layout: page
title: windows/get-wuhistory (English)
description: "Get the history of installed updates from Windows Update. Part of external `PSWindowsUpdate` module."
content_hash: c3aa5cf32edf99d1916aa697f7b230f77b91b2ec
last_modified_at: 2023-12-01
tldri18n_status: 2
---
# Get-WUHistory

Get the history of installed updates from Windows Update. Part of external `PSWindowsUpdate` module.
This command can only be run under PowerShell.
More information: <https://github.com/mgajda83/PSWindowsUpdate>.

- Get list of update history:

`Get-WUHistory`

- List the last 10 installed updates:

`Get-WUHistory -Last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- List all updates installed from a specific date to today:

`Get-WUHistory -MaxDate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">date</span>

- List all updates installed in the past 24 hours:

`Get-WUHistory -MaxDate (Get-Date).AddDays(-1)`

- Send the results via email (SMTP):

`Get-WUHistory -SendReport -PSWUSettings @{SmtpServer="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_server</span>`"; Port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_port</span>` From="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sender_email</span>`" To="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">receiver_email</span>`"}`
