---
layout: page
title: common/clear (English)
description: "Clears the screen of the terminal."
content_hash: c389de0bfe0cffc167d3ecaf31a4d5c399094439
related_topics:
  - title: Deutsch version
    url: /de/common/clear.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/clear.html
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
  - title: português (Brasil) version
    url: /pt_BR/common/clear.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/clear.html
    icon: bi bi-globe
---
# clear

Clears the screen of the terminal.
More information: <https://manned.org/clear>.

- Clear the screen (equivalent to pressing Control-L in Bash shell):

`clear`

- Clear the screen but keep the terminal's scrollback buffer:

`clear -x`

- Indicate the type of terminal to clean (defaults to the value of the environment variable `TERM`):

`clear -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type_of_terminal</span>

- Show the version of `ncurses` used by `clear`:

`clear -V`
