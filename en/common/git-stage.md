---
layout: page
title: common/git-stage (English)
description: "Add file contents to the staging area."
content_hash: 48ece0a0d9db1c798c621a81df261914202f0f03
related_topics:
  - title: français version
    url: /fr/common/git-stage.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-stage.html
    icon: bi bi-globe
---
# git stage

Add file contents to the staging area.
Synonym of `git add`.
More information: <https://git-scm.com/docs/git-stage>.

- Add a file to the index:

`git stage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Add all files (tracked and untracked):

`git stage -A`

- Only add already tracked files:

`git stage -u`

- Also add ignored files:

`git stage -f`

- Interactively stage parts of files:

`git stage -p`

- Interactively stage parts of a given file:

`git stage -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Interactively stage a file:

`git stage -i`
