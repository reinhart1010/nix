---
layout: page
title: common/dash (English)
description: "Debian Almquist Shell, a modern, POSIX-compliant implementation of `sh` (not Bash-compatible)."
content_hash: 3dc7058299d3f84deba3b4493cdabce9ba3ab8ee
related_topics:
  - title: français version
    url: /fr/common/dash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dash.html
    icon: bi bi-globe
---
# dash

Debian Almquist Shell, a modern, POSIX-compliant implementation of `sh` (not Bash-compatible).
More information: <https://manned.org/dash>.

- Start an interactive shell session:

`dash`

- Execute a command and then exit:

`dash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Execute a script:

`dash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Run commands from a script, printing each command before executing it:

`dash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Execute commands from a script, stopping at the first error:

`dash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Read and execute commands from stdin:

`dash -s`
