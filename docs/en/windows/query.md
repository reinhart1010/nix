---
layout: page
title: windows/query (English)
description: "Display information about user sessions and process."
content_hash: dc58cadf6a728e3ca74137e6a80b8e2801ee3dcf
last_modified_at: 2024-04-18
tldri18n_status: 2
---
# query

Display information about user sessions and process.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/query>.

- Display all user sessions:

`query session`

- Display the current user sessions on a remote computer:

`query session /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Display logged in users:

`query user`

- Display all user sessions on a remote computer:

`query session /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Display all running processes:

`query process`

- Display running processes by session or user name:

`query process `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name|user_name</span>
