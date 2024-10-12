---
layout: page
title: common/rustup-init.sh (한국어)
description: "`rustup` 및 Rust 툴체인을 설치하는 스크립트."
content_hash: d69e3ad6c5ef949bef3c1cc552e0c95d2096d099
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/rustup-init.sh.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rustup-init.sh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustup-init.sh

`rustup` 및 Rust 툴체인을 설치하는 스크립트.
더 많은 정보: <https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>.

- `rustup` 및 기본 Rust 툴체인을 설치하기 위해 `rustup-init` 다운로드 및 실행:

`curl https://sh.rustup.rs -sSf | sh -s`

- `rustup-init` 다운로드 및 실행하고 인자를 전달:

`curl https://sh.rustup.rs -sSf | sh -s -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인자</span>

- `rustup-init` 실행 및 추가 구성 요소나 타겟 지정하여 설치:

`rustup-init.sh --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟</span>` --component `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_요소</span>

- `rustup-init` 실행 및 설치할 기본 툴체인 지정:

`rustup-init.sh --default-toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">툴체인</span>

- `rustup-init` 실행하고 툴체인 설치하지 않기:

`rustup-init.sh --default-toolchain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none</span>

- `rustup-init` 실행 및 설치 프로필 지정:

`rustup-init.sh --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minimal|default|complete</span>

- 확인 요청 없이 `rustup-init` 실행:

`rustup-init.sh -y`
