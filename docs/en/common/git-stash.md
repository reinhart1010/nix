---
layout: page
title: common/git-stash (English)
description: "Stash local Git changes in a temporary area."
content_hash: e97ba912ea8be6a9a5582f928f299b9b74ac338d
last_modified_at: 2023-12-31
related_topics:
  - title: español version
    url: /es/common/git-stash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-stash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-stash.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-stash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git stash

Stash local Git changes in a temporary area.
More information: <https://git-scm.com/docs/git-stash>.

- Stash current changes, except new (untracked) files:

`git stash push -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_message</span>

- Stash current changes, including new (untracked) files:

`git stash -u`

- Interactively select parts of changed files for stashing:

`git stash -p`

- List all stashes (shows stash name, related branch and message):

`git stash list`

- Show the changes as a patch between the stash (default is `stash@{0}`) and the commit back when stash entry was first created:

`git stash show -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stash@{0}</span>

- Apply a stash (default is the latest, named stash@{0}):

`git stash apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_name_or_commit</span>

- Drop or apply a stash (default is stash@{0}) and remove it from the stash list if applying doesn't cause conflicts:

`git stash pop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_name</span>

- Drop all stashes:

`git stash clear`
