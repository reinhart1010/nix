---
layout: page
title: common/rustup-toolchain (한국어)
description: "Rust 툴체인 관리."
content_hash: b1ece09501fe788f9d79c9fa0ef934ac60bb81e1
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/rustup-toolchain.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustup-toolchain.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustup toolchain

Rust 툴체인 관리.
툴체인에 대한 자세한 정보는 `rustup help toolchain`을 참조.
더 많은 정보: <https://rust-lang.github.io/rustup>.

- 주어진 툴체인 설치 또는 업데이트:

`rustup install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>

- 툴체인 제거:

`rustup uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>

- 설치된 툴체인 나열:

`rustup list`

- 디렉토리에 대한 심볼릭 링크를 통해 사용자 지정 툴체인 생성:

`rustup link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_지정_툴체인_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
