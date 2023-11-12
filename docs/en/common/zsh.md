---
layout: page
title: common/zsh (English)
description: "Z SHell, a Bash-compatible command-line interpreter."
content_hash: 06571ac85942cf97eea77b466a80848f35b7ffc9
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/zsh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/zsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/zsh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zsh.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zsh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/zsh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zsh

Z SHell, a Bash-compatible command-line interpreter.
See also: `bash`, `histexpand`.
More information: <https://www.zsh.org>.

- Start an interactive shell session:

`zsh`

- Execute specific [c]ommands:

`zsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>`"`

- Execute a specific script:

`zsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.zsh</span>

- Check a specific script for syntax errors without executing it:

`zsh --no-exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.zsh</span>

- Execute specific commands from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hello world</span>` | zsh`

- Execute a specific script, printing each command in the script before executing it:

`zsh --xtrace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.zsh</span>

- Start an interactive shell session in verbose mode, printing each command before executing it:

`zsh --verbose`

- Execute a specific command inside `zsh` with disabled glob patterns:

`noglob `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
