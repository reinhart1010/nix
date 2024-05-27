---
layout: page
title: common/history (English)
description: "Command-line history."
content_hash: c56a5342d980c50ddaf9e3a89200ee8b8c470ca1
last_modified_at: 2024-05-27
related_topics:
  - title: español version
    url: /es/common/history.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/history.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/history.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/history.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/history.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/history.html
    icon: bi bi-globe
tldri18n_status: 2
---
# history

Command-line history.
More information: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Display the commands history list with line numbers:

`history`

- Display the last 20 commands (in Zsh it displays all commands starting from the 20th):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Display history with timestamps in different formats (only available in Zsh):

`history -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|f|i|E</span>

- [c]lear the commands history list (only for current Bash shell):

`history -c`

- Over[w]rite history file with history of current Bash shell (often combined with `history -c` to purge history):

`history -w`

- [d]elete the history entry at the specified offset:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">offset</span>
