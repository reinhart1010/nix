---
layout: page
title: linux/legit (English)
description: "Complementary command-line interface for Git."
content_hash: 5a1c3348c49f473dc641c60acc169e7cf1b48b5b
---
# legit

Complementary command-line interface for Git.
More information: <https://frostming.github.io/legit>.

- Switch to a specified branch, stashing and restoring unstaged changes:

`git switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_branch</span>

- Synchronize current branch, automatically merging or rebasing, and stashing and unstashing:

`git sync`

- Publish a specified branch to the remote server:

`git publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Remove a branch from the remote server:

`git unpublish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- List all branches and their publication status:

`git branches `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">glob_pattern</span>

- Remove the last commit from the history:

`git undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--hard</span>
