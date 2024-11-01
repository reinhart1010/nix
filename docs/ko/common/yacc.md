---
layout: page
title: common/yacc (한국어)
description: "형식 문법 명세 파일로 LALR 파서를 (C 언어로) 생성합니다."
content_hash: 2702efa49ebb60c83b8c4a94cc5258df38167416
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yacc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/yacc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yacc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yacc

형식 문법 명세 파일로 LALR 파서를 (C 언어로) 생성합니다.
같이 보기: `bison`.
더 많은 정보: <https://manned.org/yacc.1p>.

- C 파서 코드가 포함된 `y.tab.c` 파일을 생성하고 모든 필요한 상수 선언과 함께 문법 파일을 컴파일합니다. (상수 선언 파일 `y.tab.h`는 `-d` 플래그가 사용될 때만 생성됩니다):

`yacc -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문법_파일.y</span>

- 문법의 모호성으로 인한 충돌 보고서와 함께 파서 설명이 포함된 문법 파일 컴파일:

`yacc -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문법_파일.y</span>` -v`

- 문법 파일을 컴파일하고, 출력 파일 이름을 `y` 대신 `prefix`로 접두사 지정:

`yacc -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문법_파일.y</span>` -v -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefix</span>
