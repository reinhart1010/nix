---
layout: page
title: common/git-psykorebase (English)
description: "Rebase a branch on top of another using a merge commit and only one conflict handling."
content_hash: 7f8fa8a2e501e6c52b646de3951c0f32efebc5d4
last_modified_at: 2023-10-16
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git psykorebase

Rebase a branch on top of another using a merge commit and only one conflict handling.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-psykorebase>.

- Rebase the current branch on top of another using a merge commit and only one conflict handling:

`git psykorebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">upstream_branch</span>

- Continue after conflicts have been handled:

`git psykorebase --continue`

- Specify the branch to rebase:

`git psykorebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">upstream_branch</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_branch</span>
