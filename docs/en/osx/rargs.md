---
layout: page
title: osx/rargs (English)
description: "Execute a command for each line of standard input."
content_hash: c4e6ba0602228daea33dbe1e070e00f28d9784ba
last_modified_at: 2023-12-01
tldri18n_status: 2
---
# rargs

Execute a command for each line of standard input.
Like `xargs`, but with pattern matching support.
More information: <https://github.com/lotabout/rargs>.

- Execute a command for every line of input, just like `xargs` (`{0}` indicates where to substitute in the text):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | rargs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` {0}`

- Do a dry run, which prints the commands that would be run instead of executing them:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | rargs -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` {0}`

- Remove the `.bak` extension from every file in a list:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | rargs -p '(.*).bak mv {0} {1}`

- Execute commands in parallel:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | rargs -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max-procs</span>

- Consider each line of input to be separated by a NUL character (`\0`) instead of a newline (`\n`):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | rargs -0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` {0}`
