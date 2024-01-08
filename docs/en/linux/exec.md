---
layout: page
title: linux/exec (English)
description: "Execute a command without creating a child process."
content_hash: 81f0acb2694355eda4a0f178e68b048c379da4f7
last_modified_at: 2024-01-08
tldri18n_status: 2
---
# exec

Execute a command without creating a child process.
More information: <https://www.gnu.org/software/bash/manual/bash.html#index-exec>.

- Execute a specific command:

`exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command -with -flags</span>

- Execute a command with a (mostly) empty environment:

`exec -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command -with -flags</span>

- Execute a command as a login shell:

`exec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command -with -flags</span>

- Execute a command with a different name:

`exec -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command -with -flags</span>
