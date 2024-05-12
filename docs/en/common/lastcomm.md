---
layout: page
title: common/lastcomm (English)
description: "Show last commands executed."
content_hash: dcfeee38983c6bc2d76a6f254501890904da90d9
last_modified_at: 2024-05-12
related_topics:
  - title: Deutsch version
    url: /de/common/lastcomm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lastcomm

Show last commands executed.
More information: <https://manpages.debian.org/latest/acct/lastcomm.1.en.html>.

- Print information about all the commands in the acct (record file):

`lastcomm`

- Display commands executed by a given user:

`lastcomm --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Display information about a given command executed on the system:

`lastcomm --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display information about commands executed on a given terminal:

`lastcomm --tty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">terminal_name</span>
