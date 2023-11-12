---
layout: page
title: common/git-commit-graph (English)
description: "Write and verify Git commit-graph files."
content_hash: f1efe392aa8641461a5cbecb3bda81e0843d1f25
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/git-commit-graph.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit-graph.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit-graph

Write and verify Git commit-graph files.
More information: <https://git-scm.com/docs/git-commit-graph>.

- Write a commit-graph file for the packed commits in the repository's local `.git` directory:

`git commit-graph write`

- Write a commit-graph file containing all reachable commits:

`git show-ref --hash | git commit-graph write --stdin-commits`

- Write a commit-graph file containing all commits in the current commit-graph file along with those reachable from `HEAD`:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` | git commit-graph write --stdin-commits --append`
