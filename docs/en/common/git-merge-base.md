---
layout: page
title: common/git-merge-base (English)
description: "Find a common ancestor of two commits."
content_hash: 0167bdcb33ccb9a396acfe036ce5eba4c3736b36
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# git merge-base

Find a common ancestor of two commits.
More information: <https://git-scm.com/docs/git-merge-base>.

- Print the best common ancestor of two commits:

`git merge-base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- Print all best common ancestors of two commits:

`git merge-base --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- Check if a commit is an ancestor of a specific commit:

`git merge-base --is-ancestor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancestor_commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
