---
layout: page
title: common/hg-remove (English)
description: "Remove specified files from the staging area."
content_hash: 6b21fe0e5bd6c998364a31076c8ef72705a6cd8d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# hg remove

Remove specified files from the staging area.
More information: <https://www.mercurial-scm.org/doc/hg.1.html#remove>.

- Remove files or directories from the staging area:

`hg remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove all staged files matching a specified pattern:

`hg remove --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Remove all staged files, excluding those that match a specified pattern:

`hg remove --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Recursively remove sub-repositories:

`hg remove --subrepos`

- Remove files from the repository that have been physically removed:

`hg remove --after`
