---
layout: page
title: common/git-blame (English)
description: "Show commit hash and last author on each line of a file."
content_hash: f0ced9daa7329f361b6c0d3a4bb94ecc1e2a4d27
related_topics:
  - title: Deutsch version
    url: /de/common/git-blame.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-blame.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-blame.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-blame.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-blame.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-blame.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-blame.html
    icon: bi bi-globe
---
# git blame

Show commit hash and last author on each line of a file.
More information: <https://git-scm.com/docs/git-blame>.

- Print file with author name and commit hash on each line:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Print file with author email and commit hash on each line:

`git blame -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Print file with author name and commit hash on each line at a specific commit:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print file with author name and commit hash on each line before a specific commit:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>`~ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
