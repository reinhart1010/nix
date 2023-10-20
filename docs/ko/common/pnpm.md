---
layout: page
title: common/pnpm (한국어)
description: "빠르고, 디스크 공간 효율적인 Node.js용 패키지 관리자."
content_hash: 05d7fa1d2e41401607a5de061e2d95edaeef23e4
last_modified_at: 2023-10-20
related_topics:
  - title: Deutsch version
    url: /de/common/pnpm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pnpm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pnpm.html
    icon: bi bi-globe
---
# pnpm

빠르고, 디스크 공간 효율적인 Node.js용 패키지 관리자.
Node.js 프로젝트 및 해당 모듈 의존성 관리.
더 많은 정보: <https://pnpm.io>.

- `package.json` 파일 생성:

`pnpm init`

- `package.json`에 의존성으로 나열된 모든 패키지를 다운로드:

`pnpm install`

- 특정 버전의 패키지를 다운로드하여 `package.json`의 의존성 목록에 추가:

`pnpm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 패키지를 다운로드하고 `package.json`의 개발([D]ev) 의존성 목록에 추가:

`pnpm add -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 패키지를 다운로드하고 전역적으로([g]lobally) 설치:

`pnpm add -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 패키지를 제거하고 `package.json`의 종속성 목록에서 제거:

`pnpm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 로컬에 설치된 모듈의 트리 출력:

`pnpm list`

- 최상위 전역적으로([g]lobally) 설치된 모듈 나열:

`pnpm list -g --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
