---
layout: page
title: common/git-add (English)
description: "Adds changed files to the index."
content_hash: be401f914e52693131eb449cabc0b32dc47c9e7d
related_topics:
  - title: Deutsch version
    url: /de/common/git-add.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-add.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-add.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-add.html
    icon: bi bi-globe
---
# git add

Adds changed files to the index.
More information: <https://git-scm.com/docs/git-add>.

- Add a file to the index:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Add all files (tracked and untracked):

`git add -A`

- Only add already tracked files:

`git add -u`

- Also add ignored files:

`git add -f`

- Interactively stage parts of files:

`git add -p`

- Interactively stage parts of a given file:

`git add -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Interactively stage a file:

`git add -i`
