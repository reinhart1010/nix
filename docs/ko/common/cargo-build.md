---
layout: page
title: common/cargo-build (한국어)
description: "로컬 패키지와 모든 종속성을 컴파일."
content_hash: a0feed70812352a8066bfc50288fa94a139dc1ac
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-build.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-build.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-build.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-build.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-build.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo build

로컬 패키지와 모든 종속성을 컴파일.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- 로컬 경로의 `Cargo.toml` 매니페이스트 파일에 의해 정의된 패키지를 빌드:

`cargo build`

- 최적화를 통해 릴리스 모드에서 아티팩트 빌드:

`cargo build --release`

- `Cargo.lock`이 최신 버전이어야 함:

`cargo build --locked`

- 작업공간에서 모든 패키지를 빌드:

`cargo build --workspace`

- 특정 패키지를 빌드:

`cargo build --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 지정된 바이너리만 빌드:

`cargo build --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 지정된 테스트 대상만 빌드:

`cargo build --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트이름</span>
