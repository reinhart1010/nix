---
layout: page
title: common/npm (한국어)
description: "JavaScript 및 Node.js 패키지 관리자."
content_hash: f59f840253087d9f4add41c2d9618fb99c733b0e
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/npm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/npm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/npm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/npm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/npm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/npm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm

JavaScript 및 Node.js 패키지 관리자.
Node.js 프로젝트 및 모듈 의존성을 관리합니다.
더 많은 정보: <https://www.npmjs.com>.

- 기본값으로 `package.json` 파일 생성 (`--yes`를 생략하면 대화식으로 진행):

`npm init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-y|--yes</span>

- package.json에 의존성으로 나열된 모든 패키지를 다운로드:

`npm install`

- 특정 버전의 패키지를 다운로드하고 `package.json`의 의존성 목록에 추가:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 최신 버전의 패키지를 다운로드하고 `package.json`의 개발 의존성 목록에 추가:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- 최신 버전의 패키지를 다운로드하여 전역적으로 설치:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 패키지를 제거하고 `package.json`의 의존성 목록에서 제거:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 로컬에 설치된 모든 의존성 나열:

`npm list`

- 전역적으로 설치된 최상위 패키지 나열:

`npm list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
