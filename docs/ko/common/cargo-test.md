---
layout: page
title: common/cargo-test (한국어)
description: "Rust 패키지의 단위 및 통합 테스트를 실행."
content_hash: 5c53ef1d5c7aceacbd2e09603976f46ff93c6861
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-test.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-test.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-test.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-test.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-test.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo test

Rust 패키지의 단위 및 통합 테스트를 실행.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- 이름에 특정 문자열이 포함된 테스트만 실행:

`cargo test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트명</span>

- 동시 실행 테스트 케이스 수 설정:

`cargo test -- --test-threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>

- 최적화를 통해, 릴리스 모드에서 아티팩트 테스트:

`cargo test --release`

- 작업공간의 모든 패키지를 테스트:

`cargo test --workspace`

- 특정 패키지에 대한 테스트를 실행:

`cargo test --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 테스트 실행의 출력을 숨기지 않고 테스트를 실행:

`cargo test -- --nocapture`
