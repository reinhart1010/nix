---
layout: page
title: linux/w (English)
description: "Display who is logged in and their processes."
content_hash: 4538177f1e85d0f6d9b6a67683c2821deb385d65
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/linux/w.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/w.html
    icon: bi bi-globe
tldri18n_status: 2
---
# w

Display who is logged in and their processes.
More information: <https://www.geeksforgeeks.org/w-command-in-linux-with-examples/>.

- Display information about all users who are currently logged in:

`w`

- Display information about a specific user:

`w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display information without including the header:

`w --no-header`

- Display information without including the login, JCPU and PCPU columns:

`w --short`
