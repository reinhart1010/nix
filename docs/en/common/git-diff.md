---
layout: page
title: common/git-diff (English)
description: "Show changes to tracked files."
content_hash: 0755c0a602dc12ed1f232616182a4453c0a54235
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/git-diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git diff

Show changes to tracked files.
More information: <https://git-scm.com/docs/git-diff>.

- Show unstaged, uncommitted changes:

`git diff`

- Show all uncommitted changes (including staged ones):

`git diff HEAD`

- Show only staged (added, but not yet committed) changes:

`git diff --staged`

- Show changes from all commits since a given date/time (a date expression, e.g. "1 week 2 days" or an ISO date):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Show only names of changed files since a given commit:

`git diff --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Output a summary of file creations, renames and mode changes since a given commit:

`git diff --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Compare a single file between two branches or commits:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_2</span>` [--] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compare different files from the current branch to other branch:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
