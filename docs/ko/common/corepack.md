---
layout: page
title: common/corepack (한국어)
description: "Node 프로젝트와 해당 패키지 관리자 사이의 브라지 역할을 하는 런타임 종속성이 없는 패키지."
content_hash: c9c434a24eab610c4f9df80b5caae127165d6553
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/corepack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# corepack

Node 프로젝트와 해당 패키지 관리자 사이의 브라지 역할을 하는 런타임 종속성이 없는 패키지.
더 많은 정보: <https://github.com/nodejs/corepack>.

- Corepack shim을 Node.js 설치 디렉터리에 추가하여 전역 명령으로 사용할 수 있도록 함:

`corepack enable`

- 특정 디렉토리에 Corepack shim을 추가함:

`corepack enable --install-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- Node.js 설치 디렉터리에서 Corepack shim을 제거:

`corepack disable`

- 특정 패키지 관리자를 준비:

`corepack prepare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_매니저</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>` --activate`

- 현재 경로의 프로젝트에 대해 구성된 패키지 관리자를 준비:

`corepack prepare`

- 전역 명령으로 설치하지 않고 패키지 관리자를 사용:

`corepack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm|pnpm|yarn</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_매니저_인자</span>

- 지정된 아카이브에서 패키지 관리자를 설치:

`corepack hydrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/corepack.tgz</span>

- 하위 명령어에 대한 도움말 표시:

`corepack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>` --help`
