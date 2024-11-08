---
layout: page
title: linux/dconf-read (한국어)
description: "dconf 데이터베이스에서 키 값을 읽습니다."
content_hash: 9e964c3e6824665597b2318c8b4754ba75bcbb93
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dconf-read.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dconf-read.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dconf-read.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dconf read

dconf 데이터베이스에서 키 값을 읽습니다.
같이 보기: `dconf`.
더 많은 정보: <https://manned.org/dconf>.

- 특정 키 값을 출력:

`dconf read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>

- 특정 키의 [d]기본 값을 출력:

`dconf read -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/키</span>
