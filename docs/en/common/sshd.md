---
layout: page
title: common/sshd (English)
description: "Secure Shell Daemon - allows remote machines to securely log in to the current machine."
content_hash: 6ce46b39aaf184c25c55601440a3693a23662e26
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/sshd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sshd

Secure Shell Daemon - allows remote machines to securely log in to the current machine.
Remote machines can execute commands as it is executed at this machine.
More information: <https://man.openbsd.org/sshd>.

- Start daemon in the background:

`sshd`

- Run sshd in the foreground:

`sshd -D`

- Run with verbose output (for debugging):

`sshd -D -d`

- Run on a specific port:

`sshd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>
