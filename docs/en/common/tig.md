---
layout: page
title: common/tig (English)
description: "A text-mode interface for Git."
content_hash: 6381236c0f1a5313d6f41034cc2a80a91276efd3
last_modified_at: 2023-11-12
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

A text-mode interface for Git.
More information: <https://github.com/jonas/tig>.

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
