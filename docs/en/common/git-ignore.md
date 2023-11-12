---
layout: page
title: common/git-ignore (English)
description: "Show/update `.gitignore` files."
content_hash: 60cd16ceefc1ba71685fe4cf7afe26bfce643f92
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/git-ignore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git ignore

Show/update `.gitignore` files.
Part of `git-extras`. See also `git ignore-io`.
More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-ignore>.

- Show the content of all global and local `.gitignore` files:

`git ignore`

- Ignore file(s) privately, updating `.git/info/exclude` file:

`git ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` --private`

- Ignore file(s) locally, updating local `.gitignore` file:

`git ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>

- Ignore file(s) globally, updating global `.gitignore` file:

`git ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_pattern</span>` --global`
