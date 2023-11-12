---
layout: page
title: common/git-graft (English)
description: "Merge commits from a specific branch into another branch and delete the source branch."
content_hash: 4cb61114511cacabc9887fba50422adbf0424bd7
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git graft

Merge commits from a specific branch into another branch and delete the source branch.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-graft>.

- Merge all commits not present on the target branch from the source branch to target branch, and delete the source branch:

`git graft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_branch</span>
