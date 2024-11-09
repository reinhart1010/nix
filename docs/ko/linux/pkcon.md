---
layout: page
title: linux/pkcon (한국어)
description: "Discover 및 Gnome 소프트웨어에서 사용하는 PackageKit 콘솔 프로그램의 명령줄 클라이언트이며 'apt'의 대안입니다."
content_hash: 9d1e3dbd49433dea13dfaf9c7c6801f1b559e95b
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pkcon.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pkcon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkcon

Discover 및 Gnome 소프트웨어에서 사용하는 PackageKit 콘솔 프로그램의 명령줄 클라이언트이며 'apt'의 대안입니다.
더 많은 정보: <https://manned.org/pkcon>.

- 패키지 설치:

`pkcon install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`pkcon remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 캐시 새로고침:

`pkcon refresh`

- 패키지 업데이트:

`pkcon update`

- 특정 패키지 검색:

`pkcon search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 사용 가능한 모든 패키지 나열:

`pkcon get-packages`
