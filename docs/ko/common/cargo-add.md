---
layout: page
title: common/cargo-add (한국어)
description: "Rust 프로젝트의 `Cargo.toml` 매니페스트에 종속성을 추가."
content_hash: dc2aa7d3ad1604af26cb4cd77e1571f3fa5c3087
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-add.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo add

Rust 프로젝트의 `Cargo.toml` 매니페스트에 종속성을 추가.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- 현재 프로젝트에 최신 버전의 종속성을 추가:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성</span>

- 특정 버전의 종속성을 추가:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 종속성을 추가하고 하나 이상의 특정 기능을 활성화:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성</span>` --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능_2</span>

- 선택적 종속성을 추가하면, 크레이트의 기능으로 노출됨:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성</span>` --optional`

- 로컬 크레이트를 종속성으로 추가:

`cargo add --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/크레이트_디렉토리</span>

- 개발 또는 빌드 종속성을 추가:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|build</span>

- 모든 기본 기능이 비활성화된 종속성을 추가:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">의존성</span>` --no-default-features`
