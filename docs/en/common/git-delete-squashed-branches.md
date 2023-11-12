---
layout: page
title: common/git-delete-squashed-branches (English)
description: "Delete branches that have been \"squashed-merged\" into a specified branch and checkout. If no branch is specified, default to the currently checked out branch."
content_hash: 03b0cf25e516c52b31758271dc0d9a769f45aa8a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git delete-squashed-branches

Delete branches that have been "squashed-merged" into a specified branch and checkout. If no branch is specified, default to the currently checked out branch.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-delete-squashed-branches>.

- Delete all branches that were "squash-merged" into the current checked out branch:

`git delete-squashed-branches`

- Delete all branches that were "squash-merged" into a specific branch:

`git delete-squashed-branches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
