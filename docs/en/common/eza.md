---
layout: page
title: common/eza (English)
description: "Modern, maintained replacement for `ls`, built on `exa`."
content_hash: 54bf1d28eaba2bd528a518178a6d11d75e721ce8
last_modified_at: 2023-11-12
related_topics:
  - title: polski version
    url: /pl/common/eza.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eza

Modern, maintained replacement for `ls`, built on `exa`.
More information: <https://github.com/eza-community/eza>.

- List files one per line:

`eza --oneline`

- List all files, including hidden files:

`eza --all`

- Long format list (permissions, ownership, size and modification date) of all files:

`eza --long --all`

- List files with the largest at the top:

`eza --reverse --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>

- Display a tree of files, three levels deep:

`eza --long --tree --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- List files sorted by modification date (oldest first):

`eza --long --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modified</span>

- List files with their headers, icons, and Git statuses:

`eza --long --header --icons --git`

- Don't list files mentioned in `.gitignore`:

`eza --git-ignore`
