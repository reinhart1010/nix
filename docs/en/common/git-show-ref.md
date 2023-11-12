---
layout: page
title: common/git-show-ref (English)
description: "Git command for listing references."
content_hash: 05837a1a06ce5b4640392a7ad482155ef78f950b
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/git-show-ref.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show-ref.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-show-ref.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git show-ref

Git command for listing references.
More information: <https://git-scm.com/docs/git-show-ref>.

- Show all refs in the repository:

`git show-ref`

- Show only heads references:

`git show-ref --heads`

- Show only tags references:

`git show-ref --tags`

- Verify that a given reference exists:

`git show-ref --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ref</span>
