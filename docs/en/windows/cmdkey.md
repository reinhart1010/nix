---
layout: page
title: windows/cmdkey (English)
description: "Create, show, and delete stored user names and passwords."
content_hash: bb6952ff98c199ca91ec32c94b02c6fe9ff3e282
last_modified_at: 2024-01-31
related_topics:
  - title: हिन्दी version
    url: /hi/windows/cmdkey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmdkey

Create, show, and delete stored user names and passwords.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey>.

- List all user credentials:

`cmdkey /list`

- Store credentials for a user that accesses a server:

`cmdkey /add:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_name</span>` /user:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_name</span>

- Delete credentials for a specific target:

`cmdkey /delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_name</span>
