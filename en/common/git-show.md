---
layout: page
title: common/git-show (English)
description: "Show various types of Git objects (commits, tags, etc.)."
content_hash: 2fc495c0edeb3c5897a8d199243265d9ba227a0d
related_topics:
  - title: español version
    url: /es/common/git-show.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-show.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show.html
    icon: bi bi-globe
---
# git show

Show various types of Git objects (commits, tags, etc.).
More information: <https://git-scm.com/docs/git-show>.

- Show information about the latest commit (hash, message, changes, and other metadata):

`git show`

- Show information about a given commit:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Show information about the commit associated with a given tag:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Show information about the 3rd commit from the HEAD of a branch:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>`~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Show a commit's message in a single line, suppressing the diff output:

`git show --oneline -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Show only statistics (added/removed characters) about the changed files:

`git show --stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Show only the list of added, renamed or deleted files:

`git show --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Show the contents of a file as it was at a given revision (e.g. branch, tag or commit):

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
