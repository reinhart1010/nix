---
layout: page
title: common/git-restore (English)
description: "Restore working tree files. Requires Git version 2.23+."
content_hash: e2c9e2622db1ba89d425f9b351f0d5bcfb2fcaa5
related_topics:
  - title: español version
    url: /es/common/git-restore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-restore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-restore.html
    icon: bi bi-globe
---
# git restore

Restore working tree files. Requires Git version 2.23+.
See also `git checkout` and `git reset`.
More information: <https://git-scm.com/docs/git-restore>.

- Restore an unstaged file to the version of the current commit (HEAD):

`git restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Restore an unstaged file to the version of a specific commit:

`git restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Discard all unstaged changes to tracked files:

`git restore :/`

- Unstage a file:

`git restore --staged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Unstage all files:

`git restore --staged :/`

- Discard all changes to files, both staged and unstaged:

`git restore --worktree --staged :/`

- Interactively select sections of files to restore:

`git restore --patch`
