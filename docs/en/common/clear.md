---
layout: page
title: common/clear (English)
description: "Clears the screen of the terminal."
content_hash: ff021721748319d8674a117c355f1469fb6f041d
last_modified_at: 2024-11-25
related_topics:
  - title: Deutsch version
    url: /de/common/clear.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/clear.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/clear.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/clear.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/clear.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clear.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clear.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clear.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/clear.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/clear.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clear

Clears the screen of the terminal.
More information: <https://manned.org/clear>.

- Clear the screen:

`clear`

- Clear the screen but keep the terminal's scrollback buffer (equivalent to pressing Ctrl + L in Bash):

`clear -x`

- Indicate the type of terminal to clean (defaults to the value of the environment variable `TERM`):

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type_of_terminal</span>

- Display the version of `ncurses` used by `clear`:

`clear -V`
