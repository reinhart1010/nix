---
layout: page
title: windows/net (English)
description: "System utility to view and modify network-related settings."
content_hash: 9d7d9c670a362c693008f97f4608651e5634fef3
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/windows/net.html
    icon: bi bi-globe
tldri18n_status: 2
---
# net

System utility to view and modify network-related settings.
More information: <https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>.

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
