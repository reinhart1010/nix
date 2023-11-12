---
layout: page
title: linux/abbr (English)
description: "Manage abbreviations for the fish shell."
content_hash: ca251fc573d103491581d3799934c703ea6df532
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/abbr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/abbr.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/abbr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/abbr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/abbr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/abbr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/abbr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abbr

Manage abbreviations for the fish shell.
User-defined words are replaced with longer phrases after they are entered.
More information: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Add a new abbreviation:

`abbr --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abbreviation_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Rename an existing abbreviation:

`abbr --rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_name</span>

- Erase an existing abbreviation:

`abbr --erase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abbreviation_name</span>

- Import the abbreviations defined on another host over SSH:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_name</span>` abbr --show | source`
