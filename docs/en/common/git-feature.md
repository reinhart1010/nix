---
layout: page
title: common/git-feature (English)
description: "Create or merge feature branches."
content_hash: 4eae00f9ead5eed01d8617bc94f76fa9cfbb2fb9
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git feature

Create or merge feature branches.
Feature branches obey the format feature/<name>.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-feature>.

- Create and switch to a new feature branch:

`git feature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature_branch</span>

- Merge a feature branch into the current branch creating a merge commit:

`git feature finish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature_branch</span>

- Merge a feature branch into the current branch squashing the changes into one commit:

`git feature finish --squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature_branch</span>

- Send changes from a specific feature branch to its remote counterpart:

`git feature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature_branch</span>` --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>
