---
layout: page
title: common/git-diff-files (English)
description: "Compare files using their sha1 hashes and modes."
content_hash: b3170b2556469c74b82e6857a93b8ed5b91bb4cb
---
# git diff-files

Compare files using their sha1 hashes and modes.
More information: <https://git-scm.com/docs/git-diff-files>.

- Compare all changed files:

`git diff-files`

- Compare only specified files:

`git diff-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Show only the names of changed files:

`git diff-files --name-only`

- Output a summary of extended header information:

`git diff-files --summary`
