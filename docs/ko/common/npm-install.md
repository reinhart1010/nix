---
layout: page
title: common/npm-install (한국어)
description: "Node 패키지 설치."
content_hash: 828a8f6d5ff7e67c376400a4c44c0b55c2c4c130
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/npm-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm install

Node 패키지 설치.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-install>.

- `package.json`에 나열된 의존성 설치:

`npm install`

- 특정 버전의 패키지를 다운로드하고 `package.json`의 의존성 목록에 추가:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 최신 버전의 패키지를 다운로드하고 `package.json`의 개발 의존성 목록에 추가:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- 최신 버전의 패키지를 다운로드하고 전역으로 설치:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>
