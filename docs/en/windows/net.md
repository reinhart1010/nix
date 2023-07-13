---
layout: page
title: windows/net (English)
description: "System utility to view and modify network-related settings."
content_hash: a2f41a4cea875cc18463817b4ed75d3742109d61
last_modified_at: 2023-07-13
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># net

System utility to view and modify network-related settings.
More information: <https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>.

- Start or stop a Windows service synchronously:

`net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>

- Make sure an SMB share is available in the current console:

`net use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\\smb_shared_folder</span>` /USER:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Show the folders currently shared over SMB:

`net share`

- Show who is using your SMB shares (run in elevated console):

`net session`

- Show users in a local security group:

`net localgroup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Administrators</span>`"`

- Add a user to the local security group (run in elevated console):

`net localgroup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Administrators</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` /add`

- Display help for a subcommand:

`net help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Display help:

`net help`
