---
layout: page
title: common/gfortran (한국어)
description: "Fortran 소스 파일을 전처리하고 컴파일한 다음 함께 어셈블하고 링크."
content_hash: 2afb6f88ba5ca28ba6ee3ce17b3cc21794127bb4
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/gfortran.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gfortran.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gfortran

Fortran 소스 파일을 전처리하고 컴파일한 다음 함께 어셈블하고 링크.
더 많은 정보: <https://gcc.gnu.org/wiki/GFortran>.

- 여러 소스 파일을 실행 파일로 컴파일:

`gfortran `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스1.f90 경로/대상/소스2.f90 ...</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_실행파일</span>

- 일반적인 경고를 표시하고, 출력에서 기호를 디버그하고, 디버깅에 영향을 주지 않고 최적화:

`gfortran `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.f90</span>` -Wall -g -Og -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_실행파일</span>

- 다른 경로의 라이브러리를 포함:

`gfortran `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.f90</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_실행파일</span>` -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/수정_또는_포함</span>` -L`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/라이브러리</span>` -l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이브러리_이름</span>

- 소스 코드를 어셈블러 명령어로 컴파일:

`gfortran -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.f90</span>

- 링크 없이 소스 코드를 객체 파일로 컴파일:

`gfortran -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.f90</span>
