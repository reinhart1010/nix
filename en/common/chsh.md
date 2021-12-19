---
layout: page
title: common/chsh (English)
description: "Change the user's login shell."
content_hash: ed318fd412bebaf8fd2076462ec87f8f3c6bedad
related_topics:
  - title: bosanski version
    url: /bs/common/chsh.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/common/chsh.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/chsh.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/chsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chsh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chsh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chsh.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/chsh.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/chsh.html
    icon: bi bi-globe
---
# chsh

Change the user's login shell.
More information: <https://manned.org/chsh>.

- Change the current user's login shell interactively:

`chsh`

- Change the login shell for a given user to Zsh:

`chsh --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/zsh</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- List available shells:

`chsh --list-shells`
