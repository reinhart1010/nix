---
layout: page
title: common/cargo-rustdoc (한국어)
description: "Rust 패키지의 문서를 작성."
content_hash: 595f860dcee37a7f711c4f64e3e553a3c199bf90
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-rustdoc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-rustdoc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-rustdoc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo rustdoc

Rust 패키지의 문서를 작성.
`cargo doc`과 유사하지만, `rustdoc`에 옵션을 전달할 수 있음. 사용 가능한 모든 옵션은 `rustdoc --help`를 참조.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

- `rustdoc`에 옵션을 전달:

`cargo rustdoc -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rustdoc_옵션</span>

- 문서 린트에 대해 경고:

`cargo rustdoc -- --warn rustdoc::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">린트_이름</span>

- 문서 린트를 무시:

`cargo rustdoc -- --allow rustdoc::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">린트_이름</span>

- 패키지 라이브러리를 문서화:

`cargo rustdoc --lib`

- 지정된 바이너리를 문서화:

`cargo rustdoc --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 지정된 예시를 문서화:

`cargo rustdoc --example `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 지정된 통합 테스트를 문서화:

`cargo rustdoc --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
