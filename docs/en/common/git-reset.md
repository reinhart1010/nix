---
layout: page
title: common/git-reset (English)
description: "Undo commits or unstage changes, by resetting the current Git HEAD to the specified state."
content_hash: 9e42f731cbd81351968ca7cb8fde2ebe8c155b24
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/git-reset.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reset.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reset.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-reset.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-reset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reset

Undo commits or unstage changes, by resetting the current Git HEAD to the specified state.
If a path is passed, it works as "unstage"; if a commit hash or branch is passed, it works as "uncommit".
More information: <https://git-scm.com/docs/git-reset>.

- Unstage everything:

`git reset`

- Unstage specific file(s):

`git reset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Interactively unstage portions of a file:

`git reset --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Undo the last commit, keeping its changes (and any further uncommitted changes) in the filesystem:

`git reset HEAD~`

- Undo the last two commits, adding their changes to the index, i.e. staged for commit:

`git reset --soft HEAD~2`

- Discard any uncommitted changes, staged or not (for only unstaged changes, use `git checkout`):

`git reset --hard`

- Reset the repository to a given commit, discarding committed, staged and uncommitted changes since then:

`git reset --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
