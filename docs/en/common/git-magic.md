---
layout: page
title: common/git-magic (English)
description: "Automate add, commit, and push routines."
content_hash: 48733d865a970af44dcd64207b822c6cf9156913
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git magic

Automate add, commit, and push routines.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-magic>.

- Commit changes with a generated message:

`git magic`

- [a]dd untracked files and commit changes with a generated message:

`git magic -a`

- Commit changes with a custom [m]essage:

`git magic -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_commit_message</span>`"`

- [e]dit the commit [m]essage before committing:

`git magic -em "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_commit_message</span>`"`

- Commit changes and [p]ush to remote:

`git magic -p`

- Commit changes with a [f]orce [p]ush to remote:

`git magic -fp`
