---
layout: page
title: windows/query (English)
description: "Displays information about user sessions and process."
content_hash: 7722c990fa5b980860982e848232bd498d49c92b
---
# query

Displays information about user sessions and process.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/query>.

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
