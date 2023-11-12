---
layout: page
title: common/git-shortlog (English)
description: "Summarizes the `git log` output."
content_hash: 85cad9e3ccfe850e58747d6263ab7f34c7881aad
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/git-shortlog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-shortlog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-shortlog.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-shortlog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git shortlog

Summarizes the `git log` output.
More information: <https://git-scm.com/docs/git-shortlog>.

- View a summary of all the commits made, grouped alphabetically by author name:

`git shortlog`

- View a summary of all the commits made, sorted by the number of commits made:

`git shortlog -n`

- View a summary of all the commits made, grouped by the committer identities (name and email):

`git shortlog -c`

- View a summary of the last 5 commits (i.e. specify a revision range):

`git shortlog HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`..HEAD`

- View all users, emails and the number of commits in the current branch:

`git shortlog -sne`

- View all users, emails and the number of commits in all branches:

`git shortlog -sne --all`
