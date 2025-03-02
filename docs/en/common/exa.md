---
layout: page
title: common/exa (English)
description: "A modern replacement for `ls` (List directory contents)."
content_hash: 369f46e817691fe3bbd692b82f7c5f95ccf98c7e
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/exa.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/exa.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/exa.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/exa.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/exa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exa

A modern replacement for `ls` (List directory contents).
More information: <https://github.com/ogham/exa>.

- List files one per line:

`exa --oneline`

- List all files, including hidden files:

`exa --all`

- Long format list (permissions, ownership, size and modification date) of all files:

`exa --long --all`

- List files with the largest at the top:

`exa --reverse --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>

- Display a tree of files, three levels deep:

`exa --long --tree --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- List files sorted by modification date (oldest first):

`exa --long --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modified</span>

- List files with their headers, icons, and Git statuses:

`exa --long --header --icons --git`

- Don't list files mentioned in `.gitignore`:

`exa --git-ignore`
