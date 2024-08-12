---
layout: page
title: common/git-stash (English)
description: "Stash local Git changes in a temporary area."
content_hash: afe5833a45b3e05b6b108c61677e6fb7b8bda431
last_modified_at: 2024-08-12
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

- Stash current changes with a [m]essage, except new (untracked) files:

`git stash push --message `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_message</span>

- Stash current changes, including new ([u]ntracked) files:

`git stash --include-untracked`

- Interactively select [p]arts of changed files for stashing:

`git stash --patch`

- List all stashes (shows stash name, related branch and message):

`git stash list`

- Show the changes as a [p]atch between the stash (default is `stash@{0}`) and the commit back when stash entry was first created:

`git stash show --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stash@{0}</span>

- Apply a stash (default is the latest, named stash@{0}):

`git stash apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_name_or_commit</span>

- Drop or apply a stash (default is stash@{0}) and remove it from the stash list if applying doesn't cause conflicts:

`git stash pop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_name</span>

- Drop all stashes:

`git stash clear`
