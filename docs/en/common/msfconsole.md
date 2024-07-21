---
layout: page
title: common/msfconsole (English)
description: "Console for the Metasploit Framework."
content_hash: 29a98e2ed7b92a9ba728b13f28b2a75149d9fc44
last_modified_at: 2024-07-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/msfconsole.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># msfconsole

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
