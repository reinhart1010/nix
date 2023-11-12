---
layout: page
title: common/git-bisect (English)
description: "Use binary search to find the commit that introduced a bug."
content_hash: a8bf8a39022ba2319121828823e50b8ab696e9aa
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-bisect.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-bisect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bisect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bisect.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bisect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bisect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bisect

Use binary search to find the commit that introduced a bug.
Git automatically jumps back and forth in the commit graph to progressively narrow down the faulty commit.
More information: <https://git-scm.com/docs/git-bisect>.

- Start a bisect session on a commit range bounded by a known buggy commit, and a known clean (typically older) one:

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bad_commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good_commit</span>

- For each commit that `git bisect` selects, mark it as "bad" or "good" after testing it for the issue:

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good|bad</span>

- After `git bisect` pinpoints the faulty commit, end the bisect session and return to the previous branch:

`git bisect reset`

- Skip a commit during a bisect (e.g. one that fails the tests due to a different issue):

`git bisect skip`

- Display a log of what has been done so far:

`git bisect log`
