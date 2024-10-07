---
layout: page
title: common/git-show-branch (한국어)
description: "브랜치와 해당 커밋을 표시."
content_hash: aa4778fccb10c65d2d42a289ee0cee9250861775
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-show-branch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-show-branch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-show-branch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-show-branch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-show-branch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git show-branch

브랜치와 해당 커밋을 표시.
더 많은 정보: <https://git-scm.com/docs/git-show-branch>.

- 브랜치의 최신 커밋 요약 표시:

`git show-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름|참조|커밋</span>

- 여러 커밋 또는 브랜치의 히스토리 비교:

`git show-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름1|참조1|커밋1 브랜치_이름2|참조2|커밋2 ...</span>

- 모든 원격 추적 브랜치 비교:

`git show-branch --remotes`

- 로컬 및 원격 추적 브랜치 모두 비교:

`git show-branch --all`

- 모든 브랜치의 최신 커밋 나열:

`git show-branch --all --list`

- 현재 브랜치와 특정 브랜치 비교:

`git show-branch --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋|브랜치_이름|참조</span>

- 상대적 이름 대신 커밋 이름 표시:

`git show-branch --sha1-name --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">현재|브랜치_이름|참조</span>

- 공통 조상 이후의 커밋을 주어진 숫자만큼 계속 표시:

`git show-branch --more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋|브랜치_이름|참조</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋|브랜치_이름|참조</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>
