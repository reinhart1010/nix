---
layout: page
title: common/cargo-pkgid (한국어)
description: "현재 작업공간의 패키지 또는 종속성에 대한 정규화된 패키지 ID 지정자를 출력."
content_hash: 64eca6ece6d5663e53ec328fa2b1f01956db7eea
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/cargo-pkgid.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-pkgid.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-pkgid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo pkgid

현재 작업공간의 패키지 또는 종속성에 대한 정규화된 패키지 ID 지정자를 출력.
더 많은 정보: <https://doc.rust-lang.org/cargo/commands/cargo-pkgid.html>.

- 현재 프로젝트에 대한 정규화된 패키지 사양을 출력:

`cargo pkgid`

- 지정된 패키지에 대한 정규화된 패키지 사양을 출력:

`cargo pkgid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">부분_패키지사양</span>
