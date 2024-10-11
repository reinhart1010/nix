---
layout: page
title: common/rustup-override (한국어)
description: "디렉터리 툴체인 오버라이드를 수정합니다."
content_hash: f5b384751ee295e7bf3a84e2299423ceaa60a3e6
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/rustup-override.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustup-override.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustup override

디렉터리 툴체인 오버라이드를 수정합니다.
툴체인에 대한 자세한 내용은 `rustup help toolchain`을 참조하세요.
더 많은 정보: <https://rust-lang.github.io/rustup>.

- 디렉터리 툴체인 오버라이드 목록 표시:

`rustup override list`

- 현재 디렉터리에 대한 오버라이드 툴체인 설정 (즉, 해당 디렉터리에서 `cargo`, `rustc` 등을 특정 툴체인으로 실행하도록 `rustup`에 지시):

`rustup override set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>

- 현재 디렉터리에 대한 툴체인 오버라이드 제거:

`rustup override unset`

- 더 이상 존재하지 않는 디렉터리에 대한 모든 툴체인 오버라이드 제거:

`rustup override unset --nonexistent`
