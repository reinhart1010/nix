---
layout: page
title: common/rustup-run (한국어)
description: "Rust 툴체인에 맞게 구성된 환경에서 명령을 실행."
content_hash: 948811ade29f387eb7fccc1a33ddc3db254189e5
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/rustup-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustup run

Rust 툴체인에 맞게 구성된 환경에서 명령을 실행.
참고: `rustup`이 관리하는 모든 명령에는 이를 위한 약식이 있습니다. 예를 들어, `cargo +nightly build`는 `rustup run nightly cargo build`와 동등합니다.
더 많은 정보: <https://rust-lang.github.io/rustup>.

- 주어진 Rust 툴체인을 사용하여 명령 실행 (`rustup help toolchain`에서 더 많은 정보 확인 가능):

`rustup run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
