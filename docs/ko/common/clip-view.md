---
layout: page
title: common/clip-view (한국어)
description: "명령줄 인터페이스 페이지 렌더링."
content_hash: 76c20b4be72a6d65576ec450d6a87d311a0fe31d
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/clip-view.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clip-view

명령줄 인터페이스 페이지 렌더링.
훨씬 더 광범위한 구문과 여러 렌더링 모드를 사용해 TlDr과 유사한 프로젝트를 렌더링.
더 많은 정보: <https://github.com/command-line-interface-pages/v2-tooling/tree/main/clip-view>.

- 특정 로컬 페이지 렌더링:

`clip-view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/페이지1.clip 경로/대상/페이지2.clip ...</span>

- 특정 원격 페이지 렌더링:

`clip-view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_이름1 페이지_이름2 ...</span>

- 특정 렌더링으로 페이지 렌더링:

`clip-view --render `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tldr|tldr-colorful|docopt|docopt-colorful</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_이름1 페이지_이름2 ...</span>

- 특정 색상 테마로 페이지 렌더링:

`clip-view --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬_테마.yaml|원격_테마_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_이름1 페이지_이름2...</span>

- 페이지 또는 테마 캐시 지우기:

`clip-view --clear-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지|테마</span>`-cache`

- 도움말 표시:

`clip-view --help`

- 버전정보 표시:

`clip-view --version`
