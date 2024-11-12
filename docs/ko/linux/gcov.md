---
layout: page
title: linux/gcov (한국어)
description: "프로그램의 테스트되지 않은 부분을 발견하는 코드 커버리지 분석 및 프로파일링 도구."
content_hash: c5028b5fdb83b991623759db9b8fbc8157e6f3c1
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/gcov.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcov

프로그램의 테스트되지 않은 부분을 발견하는 코드 커버리지 분석 및 프로파일링 도구.
코드 세그먼트의 실행 빈도로 주석이 추가된 소스 코드의 복사본도 표시합니다.
더 많은 정보: <https://gcc.gnu.org/onlinedocs/gcc/Invoking-Gcov.html>.

- `file.cpp.gcov`라는 이름의 커버리지 보고서 생성:

`gcov `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.cpp</span>

- 각 기본 블록에 대한 개별 실행 횟수 기록:

`gcov --all-blocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>

- 분기 빈도를 출력 파일에 기록하고 요약 정보를 백분율로 `stdout`에 출력:

`gcov --branch-probabilities `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>

- 백분율이 아닌 실행된 분기의 수로 분기 빈도 기록:

`gcov --branch-counts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>

- `gcov` 출력 파일 생성 안 함:

`gcov --no-output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>

- 파일 수준 및 함수 수준 요약을 기록:

`gcov --function-summaries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cpp</span>
