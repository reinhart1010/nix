---
layout: page
title: common/git-merge (English)
description: "Merge branches."
content_hash: e3a06d255fe6cfa7f9ced906620f35ae730755d8
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/git-merge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-merge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-merge.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-merge.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-merge.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git merge

Merge branches.
More information: <https://git-scm.com/docs/git-merge>.

- Merge a branch into your current branch:

`git merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Edit the merge message:

`git merge --edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Merge a branch and create a merge commit:

`git merge --no-ff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Abort a merge in case of conflicts:

`git merge --abort`

- Merge using a specific strategy:

`git merge --strategy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">strategy</span>` --strategy-option `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">strategy_option</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
