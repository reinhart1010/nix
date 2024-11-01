---
layout: page
title: common/zig (한국어)
description: "Zig 컴파일러 및 툴체인."
content_hash: e1aa24584af3e84cd1ff0dd9d2e30fdfba925a9a
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zig

Zig 컴파일러 및 툴체인.
더 많은 정보: <https://ziglang.org>.

- 현재 디렉토리의 프로젝트 컴파일:

`zig build`

- 현재 디렉토리의 프로젝트 컴파일 및 실행:

`zig build run`

- `zig build` 애플리케이션 초기화:

`zig init-exe`

- `zig build` 라이브러리 초기화:

`zig init-lib`

- 테스트 빌드 생성 및 실행:

`zig test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zig</span>

- Zig 소스 코드를 표준 형식으로 재포맷:

`zig fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zig</span>

- Zig를 C 컴파일러로 사용:

`zig cc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.c</span>

- Zig를 C++ 컴파일러로 사용:

`zig c++ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>
