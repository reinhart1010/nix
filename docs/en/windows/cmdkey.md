---
layout: page
title: windows/cmdkey (English)
description: "Create, show, and delete stored user names and passwords."
content_hash: fb5a65e164dbb9492f712757d208bc964423942a
last_modified_at: 2023-06-30
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cmdkey

Create, show, and delete stored user names and passwords.
More information: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey>.

- Show a list of all user credentials:

`cmdkey /list`

- Store credentials for a user that accesses a server:

`cmdkey /add:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_name</span>` /user:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_name</span>

- Delete credentials for a specific target:

`cmdkey.exe /delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>
