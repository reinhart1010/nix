---
layout: page
title: common/yarn (한국어)
description: "JavaScript 및 Node.js 패키지 대체 관리자."
content_hash: c869bfbb43401104c1b491e95da655ae036033ee
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/yarn.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/yarn.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/yarn.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/yarn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yarn

JavaScript 및 Node.js 패키지 대체 관리자.
더 많은 정보: <https://yarnpkg.com>.

- 전역적으로 모듈 설치:

`yarn global add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- `package.json` 파일에 참조된 모든 의존성을 설치 ( `install`은 선택 사항입니다):

`yarn install`

- 모듈을 설치하고 `package.json` 파일에 대한 의존성으로 저장 (개발 전용 의존성으로 추가하려면 `--dev` 추가):

`yarn add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 모듈을 제거하고 `package.json` 파일에서 제거:

`yarn remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 대화형으로 `package.json` 파일 생성:

`yarn init`

- 모듈이 의존성인지 확인하고, 해당 모듈에 의존성이 있는 다른 모듈을 나열:

`yarn why `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>
