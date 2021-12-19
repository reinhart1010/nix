---
layout: page
title: common/zoxide (English)
description: "Keep track of the most frequently used directories."
content_hash: 397881b9066f3241feea8b4f3e03b199642a879b
related_topics:
  - title: français version
    url: /fr/common/zoxide.html
    icon: bi bi-globe
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

- Remove a directory from `zoxide`'s database:

`zoxide remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Generate shell configuration for command aliases (`z`, `za`, `zi`, `zq`, `zr`):

`zoxide init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|zsh</span>
