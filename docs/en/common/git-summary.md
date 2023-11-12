---
layout: page
title: common/git-summary (English)
description: "Display information about a Git repository."
content_hash: f285a88c4cde34386a18f6640b434fead59354da
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git summary

Display information about a Git repository.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-summary>.

- Display data about a Git repository:

`git summary`

- Display data about a Git repository since a commit-ish:

`git summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|branch_name|tag_name</span>

- Display data about a Git repository, merging committers using different emails into 1 statistic for each author:

`git summary --dedup-by-email`

- Display data about a Git repository, showing the number of lines modified by each contributor:

`git summary --line`
