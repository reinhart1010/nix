---
layout: page
title: linux/nologin (English)
description: "Alternative shell that prevents a user from logging in."
content_hash: 638db74d179420d8982c24236d82b75e526da729
related_topics:
  - title: Deutsch version
    url: /de/linux/nologin.html
    icon: bi bi-globe
---
# nologin

Alternative shell that prevents a user from logging in.

- Set a user's login shell to `nologin` to prevent the user from logging in:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` nologin`

- Customize message for users with the login shell of `nologin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">declined_login_message</span>`" > /etc/nologin.txt`
