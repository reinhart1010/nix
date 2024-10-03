---
layout: page
title: common/cargo-generate-lockfile (한국어)
description: "현재 패키지에 대한 `Cargo.lock` 파일을 생성. `cargo update`와 유사하지만, 옵션이 더 적음."
content_hash: a76c1897eb4451077d8782925847dfca79e6753f
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-generate-lockfile.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-generate-lockfile.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-generate-lockfile.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo generate-lockfile

현재 패키지에 대한 `Cargo.lock` 파일을 생성. `cargo update`와 유사하지만, 옵션이 더 적음.
잠금 파일이 이미 존재하는 경우, 모든 패키지의 최신 버전으로 다시 빌드됨.
더 많은 정보: <https://doc.rust-lang.org/stable/cargo/commands/cargo-generate-lockfile.html>.

- 모든 패키지의 최신 버전으로 `Cargo.lock` 파일을 생성:

`cargo generate-lockfile`
