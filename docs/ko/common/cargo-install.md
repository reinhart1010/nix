---
layout: page
title: common/cargo-install (한국어)
description: "Rust 바이너리를 빌드하고 설치."
content_hash: 5295d0ec35a26a9d73a8633e1043472a84d8768c
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-install.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo install

Rust 바이너리를 빌드하고 설치.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-install.html>.

- <https://crates.io>에서 패키지를 설치 (버전은 선택사항 - 기본적으로 최신버전):

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 지정된 Git 저장소에서 패키지를 설치:

`cargo install --git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>

- Git 저장소에서 설치할 떄 지정된 분기/태그/커밋에서 빌드:

`cargo install --git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_주소</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch|tag|rev</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름|태그|커밋_해쉬</span>

- 설치된 모든 패키지와 해당 버전을 나열:

`cargo install --list`
