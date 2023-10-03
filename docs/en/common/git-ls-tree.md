---
layout: page
title: common/git-ls-tree (English)
description: "List the contents of a tree object."
content_hash: 7fa430e4f973e4de7415270cfc8871f39d61b252
last_modified_at: 2023-10-03
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
  - title: Türkçe version
    url: /tr/common/git-ls-tree.html
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

- Print the filenames of the current branch head in a tree structure (Note: `tree --fromfile` is not supported on Windows):

`git ls-tree -r --name-only HEAD | tree --fromfile`
