---
layout: page
title: common/git-clean (English)
description: "Remove files not tracked by Git from the working tree."
content_hash: 9266f161178d0095999db93c0338f0a29ea154c5
last_modified_at: 2024-02-24
related_topics:
  - title: español version
    url: /es/common/git-clean.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clean.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clean.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clean.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clean

Remove files not tracked by Git from the working tree.
More information: <https://git-scm.com/docs/git-clean>.

- Delete untracked files:

`git clean`

- [i]nteractively delete untracked files:

`git clean -i`

- Show which files would be deleted without actually deleting them:

`git clean --dry-run`

- [f]orcefully delete untracked files:

`git clean -f`

- [f]orcefully delete untracked [d]irectories:

`git clean -fd`

- Delete untracked files, including e[x]cluded files (files ignored in `.gitignore` and `.git/info/exclude`):

`git clean -x`
