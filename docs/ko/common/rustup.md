---
layout: page
title: common/rustup (한국어)
description: "Rust 툴체인을 설치, 관리 및 업데이트."
content_hash: 3111df943270109f6ad897cec983ac09e2ec351e
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/rustup.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rustup.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustup.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustup

Rust 툴체인을 설치, 관리 및 업데이트.
`toolchain`, `target`, `update` 등의 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://rust-lang.github.io/rustup>.

- 시스템에 nightly 툴체인 설치:

`rustup install nightly`

- 기본 툴체인을 nightly로 전환하여 `cargo` 및 `rustc` 명령이 이를 사용하도록 설정:

`rustup default nightly`

- 현재 프로젝트 내에서만 nightly 툴체인을 사용하고 전역 설정은 변경하지 않음:

`rustup override set nightly`

- 모든 툴체인 업데이트:

`rustup update`

- 설치된 툴체인 나열:

`rustup show`

- 특정 툴체인으로 `cargo build` 실행:

`rustup run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>` cargo build`

- 기본 웹 브라우저에서 로컬 Rust 문서 열기:

`rustup doc`
