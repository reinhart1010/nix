---
layout: page
title: common/git-commit-tree (English)
description: "Low level utility to create commit objects."
content_hash: e3936250d22a8461cc4e82308de8d1474b0cb0a4
related_topics:
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

- Create a commit object reading the message from a file (use `-` for stdin):

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Create a GPG-signed commit object:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" --gpg-sign`

- Create a commit object with the specified parent commit object:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parent_commit_sha</span>
