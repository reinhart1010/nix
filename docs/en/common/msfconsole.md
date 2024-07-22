---
layout: page
title: common/msfconsole (English)
description: "Console for the Metasploit Framework."
content_hash: 29a98e2ed7b92a9ba728b13f28b2a75149d9fc44
last_modified_at: 2024-07-22
tldri18n_status: 2
---
# msfconsole

Console for the Metasploit Framework.
More information: <https://docs.rapid7.com/metasploit/msf-overview>.

- Launch the console:

`msfconsole`

- Launch the console [q]uietly without any banner:

`msfconsole --quiet`

- Do [n]ot enable database support:

`msfconsole --no-database`

- E[x]ecute console commands (Note: use `;` for passing multiple commands):

`msfconsole --execute-command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">use auxiliary/server/capture/ftp; set SRVHOST 0.0.0.0; set SRVPORT 21; run</span>`"`

- Display [v]ersion:

`msfconsole --version`
