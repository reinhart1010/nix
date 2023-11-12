---
layout: page
title: common/ksh (English)
description: "Korn Shell, a Bash-compatible command-line interpreter."
content_hash: e3421829c624baa9b222ba88951750624dc6a4a8
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/ksh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ksh

Korn Shell, a Bash-compatible command-line interpreter.
See also: `histexpand`.
More information: <http://kornshell.com>.

- Start an interactive shell session:

`ksh`

- Execute specific [c]ommands:

`ksh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'ksh is executed'</span>`"`

- Execute a specific script:

`ksh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.ksh</span>

- Check a specific script for syntax errors without executing it:

`ksh -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.ksh</span>

- Execute a specific script, printing each command in the script before executing it:

`ksh -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.ksh</span>
