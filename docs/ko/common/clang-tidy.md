---
layout: page
title: common/clang-tidy (한국어)
description: "정적 분석을 통해 스타일 위반, 버그 및 보안 결함을 찾는 LLVM 기반 C/C++ 린트 프로그램입니다."
content_hash: a5029ee244b8090fdfe0c0217ad2c8ac0b57d3d9
last_modified_at: 2024-10-04
related_topics:
  - title: Deutsch version
    url: /de/common/clang-tidy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/clang-tidy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clang-tidy

정적 분석을 통해 스타일 위반, 버그 및 보안 결함을 찾는 LLVM 기반 C/C++ 린트 프로그램입니다.
더 많은 정보: <https://clang.llvm.org/extra/clang-tidy/>.

- 소스 파일에 대한 기본 검사를 실행:

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>

- 파일에 대해 `cppcoreguidelines` 검사 이외의 검사를 실행하지 않음:

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>` -checks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-*,cppcoreguidelines-*</span>

- 사용 가능한 모든 검사를 나열:

`clang-tidy -checks=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*</span>` -list-checks`

- 컴파일 옵션으로 정의 및 포함을 지정 (`--` 뒤에서):

`clang-tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>` -- -I`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내_프로젝트/포함</span>` -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정의</span>
