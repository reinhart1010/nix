---
layout: page
title: common/git-clean (English)
description: "Remove untracked files from the working tree."
content_hash: bb4cec432fdca5b8ecaddcf9066256d970a90c48
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
  - title: தமிழ் version
    url: /ta/common/git-clean.html
    icon: bi bi-globe
---
# git clean

Remove untracked files from the working tree.
More information: <https://git-scm.com/docs/git-clean>.

- Delete files that are not tracked by Git:

`git clean`

- Interactively delete files that are not tracked by Git:

`git clean -i`

- Show what files would be deleted without actually deleting them:

`git clean --dry-run`

- Forcefully delete files that are not tracked by Git:

`git clean -f`

- Forcefully delete directories that are not tracked by Git:

`git clean -fd`

- Delete untracked files, including ignored files in `.gitignore` and `.git/info/exclude`:

`git clean -x`
