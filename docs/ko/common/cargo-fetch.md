---
layout: page
title: common/cargo-fetch (한국어)
description: "네트워크에서 패키지의 종속성을 가져옴."
content_hash: ab3caca8cf5d41f4ef86f453fb33ce8c082a4ef8
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-fetch.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-fetch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-fetch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo fetch

네트워크에서 패키지의 종속성을 가져옴.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-fetch.html>.

- `Cargo.lock`에 지정된 종속성 가져오기 (모든 대상에 대해):

`cargo fetch`

- 지정된 대상에 대한 종속성을 가져옴:

`cargo fetch --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_아키텍처_정보</span>
