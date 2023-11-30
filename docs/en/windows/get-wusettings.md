---
layout: page
title: windows/get-wusettings (English)
description: "Get the current Windows Update Agent configuration. Part of external `PSWindowsUpdate` module."
content_hash: 459d2e36c76923d0dfba8fd17f1de965e8a41cb2
last_modified_at: 2023-11-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/get-wusettings.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Get-WUSettings

Get the current Windows Update Agent configuration. Part of external `PSWindowsUpdate` module.
This command can only be run under PowerShell.
More information: <https://github.com/mgajda83/PSWindowsUpdate>.

- Get the current Windows Update Agent configuration:

`Get-WUSettings`

- Send the current configuration data via email (SMTP):

`Get-WUSettings -SendReport -PSWUSettings @{SmtpServer="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_server</span>`"; Port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_port</span>` From="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sender_email</span>`" To="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">receiver_email</span>`"}`
