---
layout: page
title: common/coproc (English)
description: "Bash builtin for creating interactive asynchronous subshells."
content_hash: ccc73ca791b5fe2cdc380831ff606e05f26f1b44
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# coproc

Bash builtin for creating interactive asynchronous subshells.
More information: <https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>.

- Run a subshell asynchronously:

`coproc { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1; command2; ...</span>`; }`

- Create a coprocess with a specific name:

`coproc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` { `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1; command2; ...</span>`; }`

- Write to a specific coprocess `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input</span>`" >&"$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{name</span>`[1]}"`

- Read from a specific coprocess `stdout`:

`read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variable</span>` <&"$`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{name</span>`[0]}"`

- Create a coprocess which repeatedly reads `stdin` and runs some commands on the input:

`coproc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` { while read line; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1; command2; ...</span>`; done }`

- Create and use a coprocess running `bc`:

`coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`
