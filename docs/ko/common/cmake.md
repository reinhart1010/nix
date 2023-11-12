---
layout: page
title: common/cmake (한국어)
description: "빌드 시스템을 생성하는 크로스 플랫폼으로 선택한 시스템에 따라 Makefiles, Visual Studio 프로젝트 또는 기타를 생성합니다."
content_hash: ef7d40aa5fc2bac6a5aff27b72f613987eb4ce9a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cmake.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cmake.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cmake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cmake.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cmake.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cmake

빌드 시스템을 생성하는 크로스 플랫폼으로 선택한 시스템에 따라 Makefiles, Visual Studio 프로젝트 또는 기타를 생성합니다.
더 많은 정보: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- 작성 파일을 생성하고 이를 사용하여 원본과 동일한 디렉토리에서 프로젝트를 컴파일합니다:

`cmake && make`

- Makefile을 생성하고 이를 사용하여 별도의 "빌드" 디렉토리(소스 외 빌드)에 프로젝트를 컴파일합니다:

`cmake -H. -B`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">빌드</span>` && make -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">빌드</span>

- 대화형 모드로 cmake를 실행 (기본값을 사용하는 대신 각 변수에 대해 요청합니다):

`cmake -i`
