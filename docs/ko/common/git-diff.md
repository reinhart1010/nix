---
layout: page
title: common/git-diff (한국어)
description: "추적된 파일의 변경 사항을 보여줍니다."
content_hash: 81f88428f854e5c48e9468466a7169fca2092c85
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/common/git-diff.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-diff.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-diff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-diff.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-diff.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-diff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git diff

추적된 파일의 변경 사항을 보여줍니다.
더 많은 정보: <https://git-scm.com/docs/git-diff>.

- 스테이지되지 않은 변경 사항 표시:

`git diff`

- 모든 커밋되지 않은 변경 사항 표시 (스테이지된 것 포함):

`git diff HEAD`

- 오직 스테이지에 있는(추가되었지만 아직 커밋되지 않은) 변경 사항만 표시:

`git diff --staged`

- 특정 일자/시간 이후의 모든 커밋부터 변경 사항 표시 (일자 표현, 예: "1 주 2 일" 또는 ISO 일자):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- 특정 커밋 이후 변경된 파일 이름만 표시:

`git diff --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 특정 커밋 이후 파일 생성, 이름 변경 및 모드 변경 요약 표시:

`git diff --summary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 두 브랜치 또는 커밋 사이의 단일 파일 비교:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_2</span>` [--] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 현재 브랜치에서 다른 브랜치로부터 다른 파일 비교:

`git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
