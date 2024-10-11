---
layout: page
title: common/rustup-set (한국어)
description: "`rustup` 설정 변경."
content_hash: d49b250af77560af8e7e63936aecbe0fa5426f3d
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/rustup-set.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustup-set.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustup set

`rustup` 설정 변경.
더 많은 정보: <https://rust-lang.github.io/rustup>.

- 기본 호스트 트리플 설정:

`rustup set default-host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_트리플</span>

- 기본 프로필 설정 (`minimal`은 `rustc`, `rust-std`, `cargo`만 포함하고, `default`는 `rust-docs`, `rustfmt`, `clippy`를 추가로 포함):

`rustup set profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minimal|default</span>

- `rustup update` 실행 시 `rustup` 자체 업데이트 여부 설정:

`rustup set auto-self-update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable|check-only</span>
