---
layout: page
title: common/git-stash (English)
description: "Stash local Git changes in a temporary area."
content_hash: 6a957ea2db4eb310d8209b3c54f7c75ee9f19863
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
---
# git stash

Stash local Git changes in a temporary area.
More information: <https://git-scm.com/docs/git-stash>.

- Stash current changes, except new (untracked) files:

`git stash [push -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_message</span>`]`

- Stash current changes, including new (untracked) files:

`git stash -u`

- Interactively select parts of changed files for stashing:

`git stash -p`

- List all stashes (shows stash name, related branch and message):

`git stash list`

- Apply a stash (default is the latest, named stash@{0}):

`git stash apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_name_or_commit</span>

- Apply a stash (default is stash@{0}), and remove it from the stash list if applying doesn't cause conflicts:

`git stash pop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_name</span>

- Drop a stash (default is stash@{0}):

`git stash drop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_name</span>

- Drop all stashes:

`git stash clear`
