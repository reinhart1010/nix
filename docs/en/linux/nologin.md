---
layout: page
title: linux/nologin (English)
description: "Alternative shell that prevents a user from logging in."
content_hash: 168835a8beaab5a46cefb40a109a6cfdb01c1d93
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/nologin.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/nologin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nologin

Alternative shell that prevents a user from logging in.
More information: <https://manned.org/nologin.5>.

- Set a user's login shell to `nologin` to prevent the user from logging in:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` nologin`

- Customize message for users with the login shell of `nologin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">declined_login_message</span>`" > /etc/nologin.txt`
