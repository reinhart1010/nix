---
layout: page
title: common/git-switch (English)
description: "Switch between Git branches. Requires Git version 2.23+."
content_hash: 267f23095da32e4f762de1471117dc380bd135ef
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-switch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-switch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-switch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-switch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-switch.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-switch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git switch

Switch between Git branches. Requires Git version 2.23+.
See also `git checkout`.
More information: <https://git-scm.com/docs/git-switch>.

- Switch to an existing branch:

`git switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create a new branch and switch to it:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Create a new branch based on an existing commit and switch to it:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Switch to the previous branch:

`git switch -`

- Switch to a branch and update all submodules to match:

`git switch --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Switch to a branch and automatically merge the current branch and any uncommitted changes into it:

`git switch --merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>
