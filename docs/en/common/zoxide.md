---
layout: page
title: common/zoxide (English)
description: "Keep track of the most frequently used directories."
content_hash: c3a180ecd4a27a35a3f1985dfe030c7c5a8f2cbc
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/zoxide.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zoxide.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zoxide

Keep track of the most frequently used directories.
Uses a ranking algorithm to navigate to the best match.
More information: <https://github.com/ajeetdsouza/zoxide>.

- Go to the highest-ranked directory that contains "foo" in the name:

`zoxide query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Go to the highest-ranked directory that contains "foo" and then "bar":

`zoxide query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Start an interactive directory search (requires `fzf`):

`zoxide query --interactive`

- Add a directory or increment its rank:

`zoxide add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Remove a directory from `zoxide`'s database interactively:

`zoxide remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --interactive`

- Generate shell configuration for command aliases (`z`, `za`, `zi`, `zq`, `zr`):

`zoxide init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|zsh</span>
