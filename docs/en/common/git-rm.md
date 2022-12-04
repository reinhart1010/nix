---
layout: page
title: common/git-rm (English)
description: "Remove files from repository index and local filesystem."
content_hash: 15c9a7665d2f576fdf7025fe1049283001bd25b2
last_modified_at: 2022-12-04
related_topics:
  - title: Deutsch version
    url: /de/common/git-rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rm.html
    icon: bi bi-globe
---
# git rm

Remove files from repository index and local filesystem.
More information: <https://git-scm.com/docs/git-rm>.

- Remove file from repository index and filesystem:

`git rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Remove directory:

`git rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Remove file from repository index but keep it untouched locally:

`git rm --cached `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
