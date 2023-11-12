---
layout: page
title: common/git-ls-files (English)
description: "Show information about files in the index and the working tree."
content_hash: 6517f1992f2b4e7766856eaf71919ad6dff95773
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/git-ls-files.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git ls-files

Show information about files in the index and the working tree.
More information: <https://git-scm.com/docs/git-ls-files>.

- Show deleted files:

`git ls-files --deleted`

- Show modified and deleted files:

`git ls-files --modified`

- Show ignored and untracked files:

`git ls-files --others`

- Show untracked files, not ignored:

`git ls-files --others --exclude-standard`
