---
layout: page
title: common/dolt-branch (한국어)
description: "Dolt 브랜치 관리."
content_hash: fecc342a4a840208e70831db90e48f9b55cd5681
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/dolt-branch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dolt-branch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dolt branch

Dolt 브랜치 관리.
더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-branch>.

- 로컬 분기 나열 (현재 분기는 `*`로 강조 표시됨):

`dolt branch`

- 모든 로컬 및 원격 브랜치를 나열:

`dolt branch --all`

- 현재 브랜치를 기반으로 새로운 브랜치를 생성:

`dolt branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 지정된 커밋을 최신으로 사용하여 새로운 브랜치를 생성:

`dolt branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 브랜치 이름 변경:

`dolt branch --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름2</span>

- 브랜치 복제:

`dolt branch --copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름2</span>

- 브랜치 삭제:

`dolt branch --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 현재 브랜치의 이름을 표시:

`dolt branch --show-current`
