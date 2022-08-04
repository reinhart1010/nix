---
layout: page
title: common/git-am (English)
description: "Apply patch files. Useful when receiving commits via email."
content_hash: 953322e4d96d9ecd388a583bcf10422aadaac040
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
  - title: தமிழ் version
    url: /ta/common/git-am.html
    icon: bi bi-globe
---
# git am

Apply patch files. Useful when receiving commits via email.
See also `git format-patch`, which can generate patch files.
More information: <https://git-scm.com/docs/git-am>.

- Apply a patch file:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.patch</span>

- Abort the process of applying a patch file:

`git am --abort`

- Apply as much of a patch file as possible, saving failed hunks to reject files:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.patch</span>
