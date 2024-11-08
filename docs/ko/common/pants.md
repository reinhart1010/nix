---
layout: page
title: common/pants (한국어)
description: "빠르고 확장 가능하며 사용자 친화적이고 오픈 소스인 빌드 및 개발자 워크플로 도구."
content_hash: 6bb22b0e8231a354c80660e95ac747277f11ccee
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/pants.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pants.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pants

빠르고 확장 가능하며 사용자 친화적이고 오픈 소스인 빌드 및 개발자 워크플로 도구.
더 많은 정보: <https://www.pantsbuild.org/2.20/docs/using-pants/command-line-help>.

- 모든 타겟 나열:

`pants list ::`

- 모든 테스트 실행:

`pants test ::`

- 커밋되지 않은 파일만 수정, 포맷, 린트 수행:

`pants --changed-since=HEAD fix fmt lint`

- 커밋되지 않은 파일과 그 종속성에 대해서만 타입 체크:

`pants --changed-since=HEAD --changed-dependents=transitive check`

- 지정된 타겟에 대한 배포 가능한 패키지 생성:

`pants package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더:타겟-이름</span>

- 새로운 소스 파일에 대한 BUILD 파일 타겟 자동 생성:

`pants tailor ::`

- 도움말 표시:

`pants help`
