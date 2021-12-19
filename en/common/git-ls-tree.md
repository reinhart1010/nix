---
layout: page
title: common/git-ls-tree (English)
description: "List the contents of a tree object."
content_hash: d6824b9b1d21a5e33a3506f8efdeccbfce17be94
related_topics:
  - title: español version
    url: /es/common/git-ls-tree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-ls-tree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-ls-tree.html
    icon: bi bi-globe
---
# git ls-tree

List the contents of a tree object.
More information: <https://git-scm.com/docs/git-ls-tree>.

- List the contents of the tree on a branch:

`git ls-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- List the contents of the tree on a commit, recursing into subtrees:

`git ls-tree -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>

- List only the filenames of the tree on a commit:

`git ls-tree --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash</span>
