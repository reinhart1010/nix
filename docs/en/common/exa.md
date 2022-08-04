---
layout: page
title: common/exa (English)
description: "A modern replacement for `ls` (List directory contents)."
content_hash: 674b07522e8b78d72c0eaf196cab05199fc16097
related_topics:
  - title: Deutsch version
    url: /de/common/exa.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/exa.html
    icon: bi bi-globe
---
# exa

A modern replacement for `ls` (List directory contents).
More information: <https://the.exa.website>.

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
