---
layout: page
title: common/git-worktree (English)
description: "Manage multiple working trees attached to the same repository."
content_hash: b178f294190af79e7474904501dc00ff4f6ef26e
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/git-worktree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-worktree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-worktree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-worktree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git worktree

Manage multiple working trees attached to the same repository.
More information: <https://git-scm.com/docs/git-worktree>.

- Create a new directory with the specified branch checked out into it:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>

- Create a new directory with a new branch checked out into it:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_branch</span>

- List all the working directories attached to this repository:

`git worktree list`

- Remove a worktree (after deleting worktree directory):

`git worktree prune`
