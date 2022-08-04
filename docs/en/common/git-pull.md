---
layout: page
title: common/git-pull (English)
description: "Fetch branch from a remote repository and merge it to local repository."
content_hash: 167a1658495ca856b352a51a699563fea35c45ac
related_topics:
  - title: Deutsch version
    url: /de/common/git-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pull.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-pull.html
    icon: bi bi-globe
---
# git pull

Fetch branch from a remote repository and merge it to local repository.
More information: <https://git-scm.com/docs/git-pull>.

- Download changes from default remote repository and merge it:

`git pull`

- Download changes from default remote repository and use fast-forward:

`git pull --rebase`

- Download changes from given remote repository and branch, then merge them into HEAD:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>
