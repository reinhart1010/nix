---
layout: page
title: common/git-status (English)
description: "Show the changes to files in a Git repository."
content_hash: 08f2d499a360400fd3c25f5c380c141035549b0b
last_modified_at: 2024-08-15
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
  - title: 한국어 version
    url: /ko/common/git-status.html
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

- Show [v]erbose information on changes in both the staging area and working directory:

`git status --verbose --verbose`

- Show the [b]ranch and tracking info:

`git status --branch`

- Show output in [s]hort format along with [b]ranch info:

`git status --short --branch`

- Show the number of entries currently stashed away:

`git status --show-stash`

- Don't show untracked files in the output:

`git status --untracked-files=no`
