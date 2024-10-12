---
layout: page
title: common/rustc (한국어)
description: "Rust 컴파일러."
content_hash: 2af972115e84f5237dfe0e17163e65bb4587f67c
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/rustc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/rustc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rustc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustc

Rust 컴파일러.
Rust 프로젝트는 보통 `rustc`를 직접 호출하는 대신 `cargo`를 사용합니다.
더 많은 정보: <https://doc.rust-lang.org/rustc>.

- 바이너리 크레이트 컴파일:

`rustc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/main.rs</span>

- 최적화하여 컴파일 (`s`는 바이너리 크기 최적화를 의미하며, `z`는 더 많은 최적화를 포함):

`rustc -C lto -C opt-level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2|3|s|z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/main.rs</span>

- 디버깅 정보 포함하여 컴파일:

`rustc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/main.rs</span>

- 오류 메시지 설명:

`rustc --explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">오류_코드</span>

- 현재 CPU에 대한 아키텍처별 최적화로 컴파일:

`rustc -C target-cpu=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">native</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/main.rs</span>

- 대상 목록 표시 (참고: 컴파일하려는 대상은 먼저 `rustup`을 사용하여 추가해야 함):

`rustc --print target-list`

- 특정 대상에 대해 컴파일:

`rustc --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_트리플</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/main.rs</span>
