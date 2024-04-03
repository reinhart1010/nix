---
layout: page
title: common/tig (English)
description: "A configurable `ncurses`-based TUI for Git."
content_hash: e2b1b5d151b71e5b52e1f683c9b5de8eafce1c27
last_modified_at: 2024-04-03
related_topics:
  - title: Deutsch version
    url: /de/common/tig.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tig

A configurable `ncurses`-based TUI for Git.
See also: `gitui`, `git-gui`.
More information: <https://jonas.github.io/tig/doc/manual.html>.

- Show the sequence of commits starting from the current one in reverse chronological order:

`tig`

- Show the history of a specific branch:

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>

- Show the history of specific files or directories:

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path1 path2 ...</span>

- Show the difference between two references (such as branches or tags):

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_ref</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compared_ref</span>

- Display commits from all branches and stashes:

`tig --all`

- Start in stash view, displaying all saved stashes:

`tig stash`

- Display help in TUI:

`h`
