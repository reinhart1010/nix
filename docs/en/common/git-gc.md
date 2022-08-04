---
layout: page
title: common/git-gc (English)
description: "Optimise the local repository by cleaning unnecessary files."
content_hash: 3a268d897289a51eb4b99308d778bf12ebf81ba6
related_topics:
  - title: español version
    url: /es/common/git-gc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-gc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-gc.html
    icon: bi bi-globe
---
# git gc

Optimise the local repository by cleaning unnecessary files.
More information: <https://git-scm.com/docs/git-gc>.

- Optimise the repository:

`git gc`

- Aggressively optimise, takes more time:

`git gc --aggressive`

- Do not prune loose objects (prunes by default):

`git gc --no-prune`

- Suppress all output:

`git gc --quiet`

- View full usage:

`git gc --help`
