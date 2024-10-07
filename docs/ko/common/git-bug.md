---
layout: page
title: common/git-bug (한국어)
description: "Git의 내부 저장소를 사용하는 분산 버그 추적기입니다. 프로젝트에 파일이 추가되지 않습니다."
content_hash: 1ee0a2331be48a250e682f8d0039aed4fb7cf56c
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-bug.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bug.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-bug.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git bug

Git의 내부 저장소를 사용하는 분산 버그 추적기입니다. 프로젝트에 파일이 추가되지 않습니다.
문제를 커밋 및 브랜치처럼 다른 사람들과 상호작용하는 동일한 Git 원격 저장소에 제출할 수 있습니다.
더 많은 정보: <https://github.com/MichaelMure/git-bug/blob/master/doc/md/git-bug.md>.

- 새 사용자 생성:

`git bug user create`

- 새 버그 생성:

`git bug add`

- 원격 저장소에 새로운 버그 항목 푸시:

`git bug push`

- 업데이트 가져오기:

`git bug pull`

- 기존 버그 나열:

`git bug ls`

- 쿼리를 사용하여 버그 필터링 및 정렬:

`git bug ls "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">상태</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열림</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정렬</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">편집</span>`"`

- 텍스트 내용으로 버그 검색:

`git bug ls "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_쿼리</span>`" baz`
