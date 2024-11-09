---
layout: page
title: linux/pacaur (한국어)
description: "Arch User Repository에서 패키지를 빌드하고 설치하기 위한 Arch Linux 유틸리티."
content_hash: ad59da5865938ae5f987a997bf71cc9a575d85ed
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pacaur.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacaur.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pacaur.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pacaur

Arch User Repository에서 패키지를 빌드하고 설치하기 위한 Arch Linux 유틸리티.
더 많은 정보: <https://github.com/rmarquis/pacaur>.

- 모든 패키지를 동기화하고 업데이트 (AUR 포함):

`pacaur -Syu`

- AUR 패키지만 동기화하고 업데이트:

`pacaur -Syua`

- 새 패키지 설치 (AUR 포함):

`pacaur -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 패키지 및 의존성 제거 (AUR 패키지 포함):

`pacaur -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 데이터베이스에서 키워드 검색 (AUR 포함):

`pacaur -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 현재 설치된 모든 패키지 나열 (AUR 패키지 포함):

`pacaur -Qs`
