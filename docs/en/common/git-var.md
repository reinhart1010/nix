---
layout: page
title: common/git-var (English)
description: "Prints a Git logical variable's value."
content_hash: 044a50c45d1df7cddca6d841248581f500ec010e
---
# git var

Prints a Git logical variable's value.
See `git config`, which is preferred over `git var`.
More information: <https://git-scm.com/docs/git-var>.

- Print the value of a Git logical variable:

`git var `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GIT_AUTHOR_IDENT|GIT_COMMITTER_IDENT|GIT_EDITOR|GIT_PAGER</span>

- [l]ist all Git logical variables:

`git var -l`
