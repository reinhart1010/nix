---
layout: page
title: linux/w (English)
description: "Display who is logged in and their processes."
content_hash: 97b36f6eef26a7f14086397bead9d2777845a418
related_topics:
  - title: 中文 version
    url: /zh/linux/w.html
    icon: bi bi-globe
---
# w

Display who is logged in and their processes.
More information: <https://www.geeksforgeeks.org/w-command-in-linux-with-examples/>.

- Display information about all users who are currently logged in:

`w`

- Display information about a specific user:

`w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Display information without including the header:

`w --no-header`

- Display information without including the login, JCPU and PCPU columns:

`w --short`
