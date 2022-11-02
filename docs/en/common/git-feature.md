---
layout: page
title: common/git-feature (English)
description: "Create or merge feature branches."
content_hash: cb83dc41719da815b7167ebd83507d75c38ca1f4
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git pull

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
