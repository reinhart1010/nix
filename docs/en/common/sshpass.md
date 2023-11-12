---
layout: page
title: common/sshpass (English)
description: "An ssh password provider."
content_hash: 345dea53528262e677b0df8e6b877486a7359c12
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/sshpass.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/sshpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sshpass

An ssh password provider.
It works by creating a TTY, feeding the password into it, and then redirecting `stdin` to the ssh session.
More information: <https://manned.org/sshpass>.

- Connect to a remote server using a password supplied on a file descriptor (in this case, `stdin`):

`sshpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Connect to a remote server with the password supplied as an option, and automatically accept unknown ssh keys:

`sshpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` ssh -o StrictHostKeyChecking=no `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Connect to a remote server using the first line of a file as the password, automatically accept unknown ssh keys, and launch a command:

`sshpass -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` ssh -o StrictHostKeyChecking=no `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`
