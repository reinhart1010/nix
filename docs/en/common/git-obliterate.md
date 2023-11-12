---
layout: page
title: common/git-obliterate (English)
description: "Delete specific files and erase their history from a Git repository."
content_hash: eb5f6a7e9b58d54788ef92a0be504ce63065003c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# git obliterate

Delete specific files and erase their history from a Git repository.
Part of `git-extras`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-obliterate>.

- Erase the existence of specific files:

`git obliterate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_1 file_2 ...</span>

- Erase the existence of specific files between 2 commits:

`git obliterate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_1 file_2 ...</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash_2</span>
