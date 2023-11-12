---
layout: page
title: common/git-repl (English)
description: "Git REPL (read-evaluate-print-loop) - an interactive Git shell."
content_hash: bd85a50d34676f0f3855debfa6e83f29c6ffb5d6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git repl

Git REPL (read-evaluate-print-loop) - an interactive Git shell.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-repl>.

- Start an interactive Git shell:

`git repl`

- Run a Git command while in the interactive Git shell:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git_subcommand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Run an external (non-Git) command while in the interactive Git shell:

`!`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Exit the interactive Git shell (or press Ctrl + D):

`exit`
