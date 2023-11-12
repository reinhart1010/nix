---
layout: page
title: common/git-prune (English)
description: "Git command for pruning all unreachable objects from the object database."
content_hash: 5f8ca8841f9c6094f20652e55f06584fb69271ad
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/git-prune.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-prune.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git prune

Git command for pruning all unreachable objects from the object database.
This command is often not used directly but as an internal command that is used by Git gc.
More information: <https://git-scm.com/docs/git-prune>.

- Report what would be removed by Git prune without removing it:

`git prune --dry-run`

- Prune unreachable objects and display what has been pruned to `stdout`:

`git prune --verbose`

- Prune unreachable objects while showing progress:

`git prune --progress`
