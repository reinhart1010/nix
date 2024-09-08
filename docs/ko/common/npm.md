---
layout: page
title: common/npm (한국어)
description: "JavaScript 및 Node.js 패키지 관리자."
content_hash: 20094a9693d75c4574a3c666425ea15417a0991f
last_modified_at: 2024-09-08
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
  - title: português (Brasil) version
    url: /pt_BR/common/npm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm

JavaScript 및 Node.js 패키지 관리자.
Node.js 프로젝트 및 모듈 의존성을 관리합니다.
더 많은 정보: <https://www.npmjs.com>.

- 대화형으로 `package.json` 파일 생성:

`npm init`

- package.json에 의존성으로 나열된 모든 패키지를 다운로드:

`npm install`

- 특정 버전의 패키지를 다운로드하여 `package.json`의 의존성 목록에 추가:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 최신 버전의 패키지를 다운로드하여 `package.json`의 개발 의존성 목록에 추가:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- 최신 버전의 패키지를 다운로드하여 전역적으로 설치:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 패키지를 제거하고 `package.json`의 의존성 목록에서 제거:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 로컬에 설치된 의존성 트리 인쇄:

`npm list`

- 전역적으로 설치된 최상위 패키지 나열:

`npm list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
