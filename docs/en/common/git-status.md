---
layout: page
title: common/git-status (English)
description: "Show the changes to files in a Git repository."
content_hash: 8205c2b612def105e6c50ede0e5dd7fba60a8cc5
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-status.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-status.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-status.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-status.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-status.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-status.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-status.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-status.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-status.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git status

Show the changes to files in a Git repository.
Lists changed, added and deleted files compared to the currently checked-out commit.
More information: <https://git-scm.com/docs/git-status>.

- Show changed files which are not yet added for commit:

`git status`

- Give output in [s]hort format:

`git status --short`

- Show the [b]ranch and tracking info:

`git status --branch`

- Show output in [s]hort format along with [b]ranch info:

`git status --short --branch`

- Show the number of entries currently stashed away:

`git status --show-stash`

- Don't show untracked files in the output:

`git status --untracked-files=no`
