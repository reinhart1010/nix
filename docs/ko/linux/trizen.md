---
layout: page
title: linux/trizen (한국어)
description: "Arch Linux에서 Arch User Repository (AUR)로부터 패키지를 빌드하는 도구."
content_hash: 3428fcb8927bd679e2d26037932589fb3166b2a3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/trizen.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/trizen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># trizen

Arch Linux에서 Arch User Repository (AUR)로부터 패키지를 빌드하는 도구.
더 많은 정보: <https://github.com/trizen/trizen>.

- 모든 AUR 패키지를 동기화하고 업데이트:

`trizen -Syua`

- 새 패키지 설치:

`trizen -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 및 의존성 제거:

`trizen -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 데이터베이스에서 키워드 검색:

`trizen -Ss `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 패키지 정보 표시:

`trizen -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 패키지 및 버전 나열:

`trizen -Qe`
