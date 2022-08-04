---
layout: page
title: linux/lastcomm (English)
description: "Show last commands executed."
content_hash: a83b47d1b2b1836bb96d8496e7a9aaefb1b1755e
related_topics:
  - title: Deutsch version
    url: /de/linux/lastcomm.html
    icon: bi bi-globe
---
# lastcomm

Show last commands executed.
More information: <https://manpages.debian.org/stable/acct/lastcomm.1.en.html>.

- Print information about all the commands in the acct (record file):

`lastcomm`

- Display commands executed by a given user:

`lastcomm --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Display information about a given command executed on the system:

`lastcomm --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display information about commands executed on a given terminal:

`lastcomm --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terminal_name</span>
