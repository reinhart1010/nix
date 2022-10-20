---
layout: page
title: common/cargo (한국어)
description: "Rust 패키지 관리프로그램."
content_hash: 46dac7a56287aa28b35e23fc93d1b42b55ddf51b
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cargo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cargo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cargo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo

Rust 패키지 관리프로그램.
Rust 프로젝트 및 해당 모듈 종속성(크레이트) 관리.
더 많은 정보: <https://crates.io>.

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
