---
layout: page
title: common/cargo (한국어)
description: "Rust 프로젝트 및 모듈 종속성(크레이트)을 관리."
content_hash: 690edbfea53c1db5e78634d03dfb474e6580c8e7
last_modified_at: 2024-10-12
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cargo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cargo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cargo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cargo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cargo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo

Rust 프로젝트 및 모듈 종속성(크레이트)을 관리.
`build`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://doc.rust-lang.org/cargo>.

- 크레이트 검색:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색할_문자열</span>

- 바이너리 크레이트 설치:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크레이트_이름</span>

- 설치된 바이너리 크레이트 나열:

`cargo install --list`

- 지정된 디렉터리(기본값은 현재 작업 디렉터리)에 새 바이너리 또는 라이브러리 Rust 프로젝트 생성:

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 현재 디렉터리의 `Cargo.toml`에 종속성 추가:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">종속성</span>

- 현재 디렉터리의 Rust 프로젝트를 릴리스 프로파일로 빌드:

`cargo build --release`

- 야간 컴파일러를 사용하여 현재 디렉터리의 Rust 프로젝트 빌드 (`rustup` 필요):

`cargo +nightly build`

- 특정 스레드 수를 사용하여 빌드 (기본값은 논리적 CPU 수):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스레드_수</span>
