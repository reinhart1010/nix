---
layout: page
title: common/git-update-index (English)
description: "Git command for manipulating the index."
content_hash: f9bea4c5a87be70951d6d947fb3ed25013205814
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/git-update-index.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-update-index.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git update-index

Git command for manipulating the index.
More information: <https://git-scm.com/docs/git-update-index>.

- Pretend that a modified file is unchanged (`git status` will not show this as changed):

`git update-index --skip-worktree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/modified_file</span>
