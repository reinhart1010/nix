---
layout: page
title: windows/get-wuapiversion (English)
description: "Get the Windows Update Agent version. Part of external `PSWindowsUpdate` module."
content_hash: 36818e1b874b7532f24837d551b50ae0d1116584
last_modified_at: 2023-12-01
tldri18n_status: 2
---
# Get-WUApiVersion

Get the Windows Update Agent version. Part of external `PSWindowsUpdate` module.
This command can only be run under PowerShell.
More information: <https://github.com/mgajda83/PSWindowsUpdate>.

- Get the currently-installed Windows Update Agent version:

`Get-WUApiVersion`

- Send the current configuration data via email (SMTP):

`Get-WUApiVersion -SendReport -PSWUSettings @{SmtpServer="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_server</span>`"; Port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smtp_port</span>` From="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sender_email</span>`" To="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">receiver_email</span>`"}`
