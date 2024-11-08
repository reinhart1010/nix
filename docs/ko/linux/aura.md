---
layout: page
title: linux/aura (한국어)
description: "Aura 패키지 관리자: Arch Linux 및 AUR를 위한 안전하고 다국어 지원 패키지 관리자."
content_hash: 66ebabe49859972b24d0f9700f4d1000c228bee4
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/aura.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aura.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/aura.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aura

Aura 패키지 관리자: Arch Linux 및 AUR를 위한 안전하고 다국어 지원 패키지 관리자.
더 많은 정보: <https://github.com/fosskers/aura>.

- 공식 저장소 및 AUR에서 패키지 검색:

`aura --aursync --both --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드|정규_표현식</span>

- AUR에서 패키지 설치:

`aura --aursync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- AUR 패키지를 자세히 모드로 업데이트하고 모든 make 의존성 제거:

`aura --aursync --diff --sysupgrade --delmakedeps --unsuppress`

- 공식 저장소에서 패키지 설치:

`aura --sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 공식 저장소에서 모든 패키지 동기화 및 업데이트:

`aura --sync --refresh --sysupgrade`

- 패키지 캐시를 사용하여 패키지 다운그레이드:

`aura --downgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 및 의존성 제거:

`aura --remove --recursive --unneeded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 고아 패키지(의존성으로 설치되었지만 더 이상 어떤 패키지도 필요로 하지 않는 패키지) 제거:

`aura --orphans --abandon`
