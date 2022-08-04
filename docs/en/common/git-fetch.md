---
layout: page
title: common/git-fetch (English)
description: "Download objects and refs from a remote repository."
content_hash: 0d39c9e597e540fab312cb876645eb6f761b330d
related_topics:
  - title: Deutsch version
    url: /de/common/git-fetch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-fetch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-fetch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-fetch.html
    icon: bi bi-globe
---
# git fetch

Download objects and refs from a remote repository.
More information: <https://git-scm.com/docs/git-fetch>.

- Fetch the latest changes from the default remote upstream repository (if set):

`git fetch`

- Fetch new branches from a specific remote upstream repository:

`git fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Fetch the latest changes from all remote upstream repositories:

`git fetch --all`

- Also fetch tags from the remote upstream repository:

`git fetch --tags`

- Delete local references to remote branches that have been deleted upstream:

`git fetch --prune`
