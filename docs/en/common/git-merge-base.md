---
layout: page
title: common/git-merge-base (English)
description: "Find a common ancestor of two commits."
content_hash: fb1a9ea6fb3686cb6a9aac1a1cd9a50e25ef0a4a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git merge-base

Find a common ancestor of two commits.
More information: <https://git-scm.com/docs/git-merge-base>.

- Print the best common ancestor of two commits:

`git merge-base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- Output all best common ancestors of two commits:

`git merge-base --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_2</span>

- Check if a commit is an ancestor of a specific commit:

`git merge-base --is-ancestor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancestor_commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
