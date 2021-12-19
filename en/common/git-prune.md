---
layout: page
title: common/git-prune (English)
description: "Git command for pruning all unreachable objects from the object database."
content_hash: 38b8c078f634925498ea39447e46cf9c5c10567d
related_topics:
  - title: italiano version
    url: /it/common/git-prune.html
    icon: bi bi-globe
---
# git prune

Git command for pruning all unreachable objects from the object database.
This command is often not used directly but as an internal command that is used by Git gc.
More information: <https://git-scm.com/docs/git-prune>.

- Report what would be removed by Git prune without removing it:

`git prune --dry-run`

- Prune unreachable objects and display what has been pruned to stdout:

`git prune --verbose`

- Prune unreachable objects while showing progress:

`git prune --progress`
