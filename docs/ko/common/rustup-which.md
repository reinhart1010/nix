---
layout: page
title: common/rustup-which (한국어)
description: "`rustup`에 의해 관리되는 명령에 대해 실행될 바이너리를 표시."
content_hash: aa86f4c90efd00c434ecd4cb1930023b575c4494
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/rustup-which.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustup-which.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustup which

`rustup`에 의해 관리되는 명령에 대해 실행될 바이너리를 표시.
`which`와 유사하지만, `$PATH` 대신 Rust 도구 체인을 검색.
더 많은 정보: <https://rust-lang.github.io/rustup>.

- 기본 도구 체인에서 바이너리의 경로 표시:

`rustup which `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 지정된 도구 체인에서 바이너리의 경로 표시 (`rustup help toolchain`에서 더 많은 정보 확인):

`rustup which --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도구_체인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
