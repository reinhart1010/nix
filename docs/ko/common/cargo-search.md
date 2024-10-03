---
layout: page
title: common/cargo-search (한국어)
description: "<https://crates.io>에서 패키지를 검색."
content_hash: 58e01782c87acff06bf5866734091bba249ea1c4
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-search.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-search.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-search.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo search

<https://crates.io>에서 패키지를 검색.
크레이트는 설명과 함께 `Cargo.toml`에 복사하기에 적합한 TOML 형식으로 표시됨.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-search.html>.

- 패키지 검색:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>

- `n` 결과 표시 (기본값: 10, 최댓값: 100):

`cargo search --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리</span>
