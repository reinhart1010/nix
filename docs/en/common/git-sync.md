---
layout: page
title: common/git-sync (English)
description: "Sync local branches with remote branches."
content_hash: f58d5d15c5a0e80313d88653d2ea442665325cef
---
# git sync

Sync local branches with remote branches.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-sync>.

- Sync the current local branch with its remote branch:

`git sync`

- Sync the current local branch with the remote main branch:

`git sync origin main`

- Sync without cleaning untracked files:

`git sync -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
