---
layout: page
title: linux/at (English)
description: "Executes commands at a specified time."
content_hash: 3d130aa9b383b023f0fad11bae70b6f62d26f0f7
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/at.html
    icon: bi bi-globe
---
# at

Executes commands at a specified time.
More information: <https://man.archlinux.org/man/at.1>.

- Open an `at` prompt to create a new set of scheduled commands, press `Ctrl + D` to save and exit:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- Execute the commands and email the result using a local mailing program such as Sendmail:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>` -m`

- Execute a script at the given time:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Display a system notification at 11pm on February 18th:

`echo "notify-send '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Wake up!</span>`'" | at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">11pm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Feb 18</span>
