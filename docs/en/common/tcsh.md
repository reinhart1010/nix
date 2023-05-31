---
layout: page
title: common/tcsh (English)
description: "C shell with file name completion and command-line editing."
content_hash: a8ffa465287f0c7bb6fa82c23e7dc3d71f8ec867
last_modified_at: 2023-05-31
---
# tcsh

C shell with file name completion and command-line editing.
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

- Execute specific commands from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'tcsh is executed'"</span>` | tcsh`
