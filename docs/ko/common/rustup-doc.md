---
layout: page
title: common/rustup-doc (한국어)
description: "현재 툴체인의 오프라인 Rust 문서를 엽니다."
content_hash: 1f3dcbe6ea4695ed7a1cdc1dd2919dc073baade6
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/rustup-doc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustup-doc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustup doc

현재 툴체인의 오프라인 Rust 문서를 엽니다.
여기서 언급되지 않은 더 많은 문서 페이지가 있습니다. 자세한 내용은 `rustup help doc`을 참조하세요.
더 많은 정보: <https://rust-lang.github.io/rustup>.

- 메인 페이지 열기:

`rustup doc`

- 특정 주제(표준 라이브러리의 모듈, 타입, 키워드 등)의 문서 열기:

`rustup doc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">std::fs|usize|fn|...</span>

- Rust 프로그래밍 언어 책 열기:

`rustup doc --book`

- Cargo 책 열기:

`rustup doc --cargo`

- Rust 레퍼런스 열기:

`rustup doc --reference`
