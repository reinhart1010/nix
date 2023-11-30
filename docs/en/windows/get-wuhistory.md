---
layout: page
title: windows/get-wuhistory (English)
description: "Get the history of installed updates from Windows Update. Part of external `PSWindowsUpdate` module."
content_hash: c3aa5cf32edf99d1916aa697f7b230f77b91b2ec
last_modified_at: 2023-11-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-wuhistory.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-WUHistory

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
