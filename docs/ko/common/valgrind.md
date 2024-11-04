---
layout: page
title: common/valgrind (한국어)
description: "프로그램의 프로파일링, 최적화 및 디버깅을 위한 전문가용 도구 세트의 래퍼."
content_hash: 3785721cbdac26d6246462d4db098178c06ce1d0
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/valgrind.html
    icon: bi bi-globe
tldri18n_status: 2
---
# valgrind

프로그램의 프로파일링, 최적화 및 디버깅을 위한 전문가용 도구 세트의 래퍼.
일반적으로 사용되는 도구로는 `memcheck`, `cachegrind`, `callgrind`, `massif`, `helgrind`, `drd`가 있습니다.
더 많은 정보: <https://www.valgrind.org>.

- (기본) Memcheck 도구를 사용하여 `program`의 메모리 사용 진단 표시:

`valgrind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- Memcheck를 사용하여 `program`의 모든 가능한 메모리 누수를 자세히 보고:

`valgrind --leak-check=full --show-leak-kinds=all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- Cachegrind 도구를 사용하여 `program`의 CPU 캐시 작업을 프로파일링하고 기록:

`valgrind --tool=cachegrind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- Massif 도구를 사용하여 `program`의 힙 메모리 및 스택 사용을 프로파일링하고 기록:

`valgrind --tool=massif --stacks=yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>
