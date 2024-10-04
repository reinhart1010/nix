---
layout: page
title: common/cargo-fmt (한국어)
description: "Rust 프로젝트의 모든 소스 파일에 대해 `rustfmt`를 실행."
content_hash: b418491df33760a4bfc5a205f4860d1478ec3408
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cargo-fmt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo fmt

Rust 프로젝트의 모든 소스 파일에 대해 `rustfmt`를 실행.
더 많은 정보: <https://github.com/rust-lang/rustfmt>.

- 모든 소스 파일 포맷:

`cargo fmt`

- 파일에 쓰지 않고 포맷 오류를 확인:

`cargo fmt --check`

- 각 `rustfmt` 호출에 인수를 전달:

`cargo fmt -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rustfmt_인수</span>
