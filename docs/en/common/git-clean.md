---
layout: page
title: common/git-clean (English)
description: "Remove files not tracked by Git from the working tree."
content_hash: 210182eaf322ad4ced9198fec813bdc20ff618a0
last_modified_at: 2024-08-31
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

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--interactive|-i</span>

- Show which files would be deleted without actually deleting them:

`git clean --dry-run`

- Forcefully delete untracked files:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--force|-f</span>

- Forcefully delete untracked [d]irectories:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--force|-f</span>` -d`

- Delete untracked files, including e[x]cluded files (files ignored in `.gitignore` and `.git/info/exclude`):

`git clean -x`
