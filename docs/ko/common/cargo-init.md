---
layout: page
title: common/cargo-init (한국어)
description: "새로운 Cargo 패키지를 생성."
content_hash: aeb2edb5a002d6ea2101f89e812674f2dc677a59
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-init.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-init.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-init.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo init

새로운 Cargo 패키지를 생성.
`cargo new`와 동일하지만, 디렉터리 지정은 선택 사항.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-init.html>.

- 현재 디렉터리의 바이너리 대상을 사용하여 Rust 프로젝트를 초기화:

`cargo init`

- 지정된 디렉터리의 바이너리 대상을 사용해 Rust 프로젝트를 초기화:

`cargo init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 현재 디렉터리의 라이브러리 대상을 사용해 Rust 프로젝트를 초기화:

`cargo init --lib`

- 프로젝트 디렉터리에서 버전 제어 시스템 저장소를 초기화 (기본값: `git`):

`cargo init --vcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git|hg|pijul|fossil|none</span>

- 패키지 이름 설정 (기본값: 디렉터리 이름):

`cargo init --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
