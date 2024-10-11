---
layout: page
title: common/rustdoc (한국어)
description: "Rust 크레이트에 대한 문서를 생성합니다."
content_hash: 0e5976da5e458caddabacf538964b397b1390aa6
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/rustdoc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustdoc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustdoc

Rust 크레이트에 대한 문서를 생성합니다.
더 많은 정보: <https://doc.rust-lang.org/stable/rustdoc>.

- 크레이트의 루트에서 문서 생성:

`rustdoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src/lib.rs</span>

- 프로젝트 이름 지정:

`rustdoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src/lib.rs</span>` --crate-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 마크다운 파일에서 문서 생성:

`rustdoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.md</span>

- 출력 디렉토리 지정:

`rustdoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">src/lib.rs</span>` --out-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_디렉토리</span>
