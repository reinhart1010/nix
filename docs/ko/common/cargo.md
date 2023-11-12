---
layout: page
title: common/cargo (한국어)
description: "Rust 패키지 관리프로그램."
content_hash: 826f0263c11b8954f47fc34bf72f3364b16760d5
last_modified_at: 2023-11-12
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo

Rust 패키지 관리프로그램.
Rust 프로젝트 및 해당 모듈 종속성(크레이트) 관리.
더 많은 정보: <https://doc.rust-lang.org/cargo>.

- 크레이트 검색:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색할_문자열</span>

- 크레이트 설치:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크레이트_이름</span>

- 설치된 크레이트 목록:

`cargo install --list`

- 현재 디렉토리에 새 이진 또는 라이브러리 Rust 프로젝트 생성:

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- 지정된 디렉토리에 새 이진 또는 라이브러리 Rust 프로젝트 생성:

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/디렉토리</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- 현재 디렉토리에 Rust 프로젝트 구축:

`cargo build`

- 특정 쓰레드 수를 사용하여 구축(기본값은 CPU 코어 수):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업</span>
