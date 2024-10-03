---
layout: page
title: common/cargo-logout (한국어)
description: "레지스트리에서 로컬로 API 토큰을 제거."
content_hash: 0d7d3518fc94cb598b40ac11110d3d431f5fad3c
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-logout.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-logout.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-logout.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo logout

레지스트리에서 로컬로 API 토큰을 제거.
토큰은 패키지 레지스트리를 인증하는 데 사용됨. `cargo login`을 사용하여 다시 추가할 수 있음.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- 로컬 자격 증명 저장소 (`$CARGO_HOME/credentials.toml`에 위치)에서 API 토큰을 제거:

`cargo logout`

- 지정된 레지스트리를 사용 (레지스트리 이름은 구성에서 정의할 수 있음 - 기본값은 <https://crates.io>):

`cargo logout --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
