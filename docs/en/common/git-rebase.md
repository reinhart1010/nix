---
layout: page
title: common/git-rebase (English)
description: "Reapply commits from one branch on top of another branch."
content_hash: 6823293f97657038a907c6c975b73a1a813a7522
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-rebase.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rebase.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rebase.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rebase.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rebase.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rebase.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-rebase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rebase

Reapply commits from one branch on top of another branch.
Commonly used to "move" an entire branch to another base, creating copies of the commits in the new location.
More information: <https://git-scm.com/docs/git-rebase>.

- Rebase the current branch on top of another specified branch:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_base_branch</span>

- Start an interactive rebase, which allows the commits to be reordered, omitted, combined or modified:

`git rebase -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_base_branch_or_commit_hash</span>

- Continue a rebase that was interrupted by a merge failure, after editing conflicting files:

`git rebase --continue`

- Continue a rebase that was paused due to merge conflicts, by skipping the conflicted commit:

`git rebase --skip`

- Abort a rebase in progress (e.g. if it is interrupted by a merge conflict):

`git rebase --abort`

- Move part of the current branch onto a new base, providing the old base to start from:

`git rebase --onto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_base</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_base</span>

- Reapply the last 5 commits in-place, stopping to allow them to be reordered, omitted, combined or modified:

`git rebase -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~5</span>

- Auto-resolve any conflicts by favoring the working branch version (`theirs` keyword has reversed meaning in this case):

`git rebase -X theirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
