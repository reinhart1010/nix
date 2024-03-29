---
layout: page
title: common/bash (English)
description: "Bourne-Again SHell, an `sh`-compatible command-line interpreter."
content_hash: f929db37030767687b820a1075dcdf07dfa93727
last_modified_at: 2024-02-19
related_topics:
  - title: Deutsch version
    url: /de/common/bash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bash.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bash.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bash.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/bash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bash

Bourne-Again SHell, an `sh`-compatible command-line interpreter.
See also: `zsh`, `histexpand` (history expansion).
More information: <https://www.gnu.org/software/bash/>.

- Start an interactive shell session:

`bash`

- Start an interactive shell session without loading startup configs:

`bash --norc`

- Execute specific [c]ommands:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'bash is executed'</span>`"`

- Execute a specific script:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- E[x]ecute a specific script, printing each command before executing it:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Execute a specific script and stop at the first [e]rror:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>

- Execute specific commands from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'bash is executed'"</span>` | bash`

- Start a [r]estricted shell session:

`bash -r`
