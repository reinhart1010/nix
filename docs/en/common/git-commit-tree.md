---
layout: page
title: common/git-commit-tree (English)
description: "Low level utility to create commit objects."
content_hash: fb40e2b41969b2517aefdc8d36a46dbbb2ae39bc
last_modified_at: 2022-12-04
related_topics:
  - title: Türkçe version
    url: /tr/common/git-commit-tree.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit-tree.html
    icon: bi bi-globe
---
# git commit-tree

Low level utility to create commit objects.
See also: `git commit`.
More information: <https://git-scm.com/docs/git-commit-tree>.

- Create a commit object with the specified message:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`"`

- Create a commit object reading the message from a file (use `-` for `stdin`):

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a GPG-signed commit object:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" --gpg-sign`

- Create a commit object with the specified parent commit object:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parent_commit_sha</span>
