---
layout: page
title: common/git-status (English)
description: "Show the changes to files in a Git repository."
content_hash: d97e24f5c72a0b1443c9daf4f91052e9b2434f67
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
  - title: українська version
    url: /uk/common/git-status.html
    icon: bi bi-globe
---
# git status

Show the changes to files in a Git repository.
Lists changed, added and deleted files compared to the currently checked-out commit.
More information: <https://git-scm.com/docs/git-status>.

- Show changed files which are not yet added for commit:

`git status`

- Give output in [s]hort format:

`git status -s`

- Don't show untracked files in the output:

`git status --untracked-files=no`

- Show output in [s]hort format along with [b]ranch info:

`git status -sb`
