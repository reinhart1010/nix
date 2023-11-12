---
layout: page
title: common/git-grep (English)
description: "Find strings inside files anywhere in a repository's history."
content_hash: 15ae6096e7913d6b98442029cb19aa477a4dad7b
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/git-grep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-grep.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-grep.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-grep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git-grep

Find strings inside files anywhere in a repository's history.
Accepts a lot of the same flags as regular `grep`.
More information: <https://git-scm.com/docs/git-grep>.

- Search for a string in tracked files:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>

- Search for a string in files matching a pattern in tracked files:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_glob_pattern</span>

- Search for a string in tracked files, including submodules:

`git grep --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>

- Search for a string at a specific point in history:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>

- Search for a string across all branches:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_string</span>` $(git rev-list --all)`
