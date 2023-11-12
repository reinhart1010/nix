---
layout: page
title: common/git-am (English)
description: "Apply patch files and create a commit. Useful when receiving commits via email."
content_hash: 2122b298185915645993dda5473a3388f3cfdf17
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-am.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-am.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-am.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git am

Apply patch files and create a commit. Useful when receiving commits via email.
See also `git format-patch`, which can generate patch files.
More information: <https://git-scm.com/docs/git-am>.

- Apply and commit changes following a local patch file:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.patch</span>

- Apply and commit changes following a remote patch file:

`curl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file.patch</span>` | git apply`

- Abort the process of applying a patch file:

`git am --abort`

- Apply as much of a patch file as possible, saving failed hunks to reject files:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.patch</span>
