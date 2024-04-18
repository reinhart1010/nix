---
layout: page
title: common/git-var (English)
description: "Print a Git logical variable's value."
content_hash: 0252174a17337ee475d594b377962a50d3efbe81
last_modified_at: 2024-04-18
related_topics:
  - title: Türkçe version
    url: /tr/common/git-var.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git var

Print a Git logical variable's value.
See `git config`, which is preferred over `git var`.
More information: <https://git-scm.com/docs/git-var>.

- Print the value of a Git logical variable:

`git var `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GIT_AUTHOR_IDENT|GIT_COMMITTER_IDENT|GIT_EDITOR|GIT_PAGER</span>

- [l]ist all Git logical variables:

`git var -l`
