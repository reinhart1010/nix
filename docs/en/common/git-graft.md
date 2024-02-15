---
layout: page
title: common/git-graft (English)
description: "Merge commits from a branch into another branch and delete the source branch."
content_hash: 97805e606306f69621961ba5547a7f58893aa923
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# git graft

Merge commits from a branch into another branch and delete the source branch.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-graft>.

- Merge all commits not present on the target branch from the source branch to target branch, and delete the source branch:

`git graft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_branch</span>
