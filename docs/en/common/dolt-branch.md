---
layout: page
title: common/dolt-branch (English)
description: "Manage Dolt branches."
content_hash: 0ce6e6c68246a543e5dcf0b26159e7a27cfff802
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# dolt branch

Manage Dolt branches.
More information: <https://docs.dolthub.com/cli-reference/cli#dolt-branch>.

- List local branches (current branch is highlighted by `*`):

`dolt branch`

- List all local and remote branches:

`dolt branch --all`

- Create a new branch based on the current branch:

`dolt branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create a new branch with the specified commit as the latest:

`dolt branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Rename a branch:

`dolt branch --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name2</span>

- Duplicate a branch:

`dolt branch --copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name2</span>

- Delete a branch:

`dolt branch --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Display the name of the current branch:

`dolt branch --show-current`
