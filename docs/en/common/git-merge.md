---
layout: page
title: common/git-merge (English)
description: "Merge branches."
content_hash: c798b89b25c3790e173bac07d1232222c559d9cc
related_topics:
  - title: español version
    url: /es/common/git-merge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-merge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-merge.html
    icon: bi bi-globe
---
# git merge

Merge branches.
More information: <https://git-scm.com/docs/git-merge>.

- Merge a branch into your current branch:

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Edit the merge message:

`git merge -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Merge a branch and create a merge commit:

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Abort a merge in case of conflicts:

`git merge --abort`
