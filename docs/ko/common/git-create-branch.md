---
layout: page
title: common/git-create-branch (한국어)
description: "리포지토리에 Git 브랜치 생성."
content_hash: 5ab34c48000c5c05e08fccc61a4b936e28a3859b
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-create-branch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-create-branch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-create-branch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git create-branch

리포지토리에 Git 브랜치 생성.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-create-branch>.

- 로컬 브랜치 생성:

`git create-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 로컬 및 origin에 브랜치 생성:

`git create-branch --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 로컬 및 upstream(포크를 통해)에 브랜치 생성:

`git create-branch --remote upstream `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>
