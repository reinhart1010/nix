---
layout: page
title: common/git-squash (English)
description: "Squash multiple commits into a single commit."
content_hash: 1df0f25a959968e05d09e383290df5f52a8984b9
---
# git squash

Squash multiple commits into a single commit.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-squash>.

- Merge all commits from a specific branch into the current branch as a single commit:

`git squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_branch</span>

- Squash all commits starting with a specific commit on the current branch:

`git squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Squash the `n` latest commits and commit with a message:

`git squash HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Squash the `n` latest commits and commit concatenating all individual messages:

`git squash --squash-msg HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>
