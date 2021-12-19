---
layout: page
title: common/git-show-branch (English)
description: "Show branches and their commits."
content_hash: a9aea40211a305f362fcfc0a6535d2ccf57c6277
related_topics:
  - title: français version
    url: /fr/common/git-show-branch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show-branch.html
    icon: bi bi-globe
---
# git show-branch

Show branches and their commits.
More information: <https://git-scm.com/docs/git-show-branch>.

- Show a summary of the latest commit on a branch:

`git show-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name|ref|commit</span>

- Compare commits in the history of multiple commits or branches:

`git show-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name|ref|commit</span>

- Compare all remote tracking branches:

`git show-branch --remotes`

- Compare both local and remote tracking branches:

`git show-branch --all`

- List the latest commits in all branches:

`git show-branch --all --list`

- Compare a given branch with the current branch:

`git show-branch --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|branch_name|ref</span>

- Display the commit name instead of the relative name:

`git show-branch --sha1-name --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current|branch_name|ref</span>

- Keep going a given number of commits past the common ancestor:

`git show-branch --more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|branch_name|ref</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit|branch_name|ref</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>
