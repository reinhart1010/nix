---
layout: page
title: common/cargo-publish (한국어)
description: "패키지를 레지스트리에 업로드."
content_hash: 98e9eb8c970d343522ca5889606c3fcf3be875a4
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-publish.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-publish.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-publish.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo publish

패키지를 레지스트리에 업로드.
참고: 패키지를 게시하기 전에 `cargo login`을 사용하여 인증 토큰을 추가해야 함.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-publish.html>.

- 검사를 수행하고, `.crate` 파일을 생성하여 레지스트리에 업로드:

`cargo publish`

- 검사를 수행하고, `.crate` 파일을 생성하여 레지스트리에 업로드하지 않음 (`cargo package`와 동일):

`cargo publish --dry-run`

- 지정된 레지스트리를 사용함 (레지스트리 이름은 구성에서 정의할 수 있음 - 기본값은 <https://crates.io>):

`cargo publish --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
