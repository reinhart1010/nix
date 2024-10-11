---
layout: page
title: common/rustfmt (한국어)
description: "Rust 소스 코드를 포맷합니다."
content_hash: 7d33b120c3cec6d776b9b2a176e42fe3f699fd52
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/rustfmt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rustfmt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/rustfmt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustfmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustfmt

Rust 소스 코드를 포맷합니다.
더 많은 정보: <https://github.com/rust-lang/rustfmt>.

- 파일을 포맷하여 원본 파일을 덮어쓰기:

`rustfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/source.rs</span>

- 파일의 포맷을 확인하고 변경 사항을 콘솔에 표시:

`rustfmt --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/source.rs</span>

- 포맷하기 전에 변경된 파일을 백업 (원본 파일은 `.bk` 확장자로 이름이 변경됩니다):

`rustfmt --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/source.rs</span>
