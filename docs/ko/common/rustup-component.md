---
layout: page
title: common/rustup-component (한국어)
description: "툴체인에 설치된 구성 요소를 수정."
content_hash: 9a7ffb4f87a66b5bcf0685b2fbf3e8d58d0902c3
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/rustup-component.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustup-component.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustup component

툴체인에 설치된 구성 요소를 수정.
`--toolchain` 옵션 없이 사용하면 `rustup`은 기본 툴체인을 사용합니다. 툴체인에 대한 자세한 내용은 `rustup help toolchain`을 참조하세요.
더 많은 정보: <https://rust-lang.github.io/rustup>.

- 툴체인에 구성 요소 추가:

`rustup component add --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소</span>

- 툴체인에서 구성 요소 제거:

`rustup component remove --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소</span>

- 툴체인에 대해 설치된 및 사용 가능한 구성 요소 나열:

`rustup component list --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>

- 툴체인에 대해 설치된 구성 요소 나열:

`rustup component list --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>` --installed`
