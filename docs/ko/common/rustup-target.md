---
layout: page
title: common/rustup-target (한국어)
description: "툴체인의 지원 대상 수정."
content_hash: 52ecb2b332c6fc48077acb0915a6d726f0326c0c
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/rustup-target.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustup target

툴체인의 지원 대상 수정.
`--toolchain` 옵션이 없으면 `rustup`은 기본 툴체인을 사용합니다. 툴체인에 대한 자세한 정보는 `rustup help toolchain`을 참조하세요.
더 많은 정보: <https://rust-lang.github.io/rustup>.

- 툴체인에 대상 추가:

`rustup target add --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 툴체인에서 대상 제거:

`rustup target remove --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 툴체인의 사용 가능 및 설치된 대상 나열:

`rustup target list --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>

- 툴체인에 설치된 대상 나열:

`rustup target list --toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>` --installed`
