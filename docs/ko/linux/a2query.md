---
layout: page
title: linux/a2query (한국어)
description: "Debian 기반 OS에서 Apache의 런타임 설정을 검색."
content_hash: ae008f97460c018520cf0c3f5fc9cf849381f2e5
last_modified_at: 2024-11-08
related_topics:
  - title: català version
    url: /ca/linux/a2query.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/a2query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/a2query.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/a2query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/a2query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/a2query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/a2query.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/a2query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/a2query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/a2query.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/a2query.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># a2query

Debian 기반 OS에서 Apache의 런타임 설정을 검색.
더 많은 정보: <https://manned.org/a2query>.

- 활성화된 Apache 모듈 나열:

`sudo a2query -m`

- 특정 모듈이 설치되어 있는지 확인:

`sudo a2query -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 활성화된 가상 호스트 나열:

`sudo a2query -s`

- 현재 활성화된 멀티 프로세싱 모듈 표시:

`sudo a2query -M`

- Apache 버전 표시:

`sudo a2query -v`
