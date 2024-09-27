---
layout: page
title: common/git-reflog (English)
description: "Show a log of changes to local references like HEAD, branches or tags."
content_hash: aa35ab10960479dcdd67ecbd6586b356e4eac23c
last_modified_at: 2024-09-27
related_topics:
  - title: español version
    url: /es/common/git-reflog.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-reflog.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-reflog.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-reflog.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-reflog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git reflog

Show a log of changes to local references like HEAD, branches or tags.
More information: <https://git-scm.com/docs/git-reflog>.

- Show the reflog for HEAD:

`git reflog`

- Show the reflog for a given branch:

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Show only the 5 latest entries in the reflog:

`git reflog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--max-count</span>` 5`
