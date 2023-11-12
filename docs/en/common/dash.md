---
layout: page
title: common/dash (English)
description: "Debian Almquist Shell, a modern, POSIX-compliant implementation of `sh` (not Bash-compatible)."
content_hash: 686f53618bee0828344c5524853959d883d389d8
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/dash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dash

Debian Almquist Shell, a modern, POSIX-compliant implementation of `sh` (not Bash-compatible).
More information: <https://manned.org/dash>.

- Start an interactive shell session:

`dash`

- Execute specific [c]ommands:

`dash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'dash is executed'</span>`"`

- Execute a specific script:

`dash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Check a specific script for syntax errors:

`dash -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Execute a specific script while printing each command before executing it:

`dash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Execute a specific script and stop at the first [e]rror:

`dash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Execute specific commands from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'dash is executed'"</span>` | dash`
