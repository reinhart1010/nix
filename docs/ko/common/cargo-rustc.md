---
layout: page
title: common/cargo-rustc (한국어)
description: "Rust 패키지를 컴파일. `cargo build`와 유사하지만, 컴파일러에 추가 옵션을 전달할 수 있음."
content_hash: 5159e82baa97d3f3b1d5b717e91c254f75bd6327
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-rustc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-rustc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-rustc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-rustc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-rustc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo rustc

Rust 패키지를 컴파일. `cargo build`와 유사하지만, 컴파일러에 추가 옵션을 전달할 수 있음.
사용 가능한 모든 옵션은 `rustc --help`를 참조.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- 패키지를 빌드하고 `rustc`에 옵션을 전달:

`cargo rustc -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rustc_옵션</span>

- 최적화를 통해 릴리스 모드에서 아티팩트 빌드:

`cargo rustc --release`

- 현재 CPU에 대한 아키텍처별 최적화로 컴파일:

`cargo rustc --release -- -C target-cpu=native`

- 속도 최적화로 컴파일:

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>

- 크기([s]ize) 최적화로 컴파일 (`z` 또한 루프 벡터화를 끔):

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|z</span>

- 패키지가 안전하지 않은 코드를 사용하는지 확인:

`cargo rustc --lib -- -D unsafe-code`

- 특정 패키지 빌드:

`cargo rustc --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 지정된 바이너리만 빌드:

`cargo --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
