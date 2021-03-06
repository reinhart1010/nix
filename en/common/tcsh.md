---
layout: page
title: common/tcsh (English)
description: "C shell with file name completion and command line editing."
content_hash: be9d7d387e7902d32de1357980011207ce925ce4
---
# tcsh

C shell with file name completion and command line editing.
See also: `csh`.
More information: <https://manned.org/tcsh>.

- Start an interactive shell session:

`tcsh`

- Start an interactive shell session without loading startup configs:

`tcsh -f`

- Execute specific [c]ommands:

`tcsh -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'tcsh is executed'</span>`"`

- Execute a specific script:

`tcsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.tcsh</span>

- Check a specific script for syntax errors:

`tcsh -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.tcsh</span>

- Execute specific commands from stdin:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'tcsh is executed'"</span>` | tcsh`
