---
layout: page
title: linux/wajig (한국어)
description: "Debian 기반 시스템을 위한 단순화된 올인원 시스템 지원 도구."
content_hash: 623854d659af124b98fcecade2608244ce75f538
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/wajig.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/wajig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wajig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wajig

Debian 기반 시스템을 위한 단순화된 올인원 시스템 지원 도구.
더 많은 정보: <https://wajig.togaware.com>.

- 사용 가능한 패키지 및 버전 목록 업데이트:

`wajig update`

- 패키지 설치 또는 최신 버전으로 업데이트:

`wajig install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 및 해당 설정 파일 제거:

`wajig purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 업데이트 후 배포 업그레이드 수행:

`wajig daily-upgrade`

- 설치된 패키지의 크기 표시:

`wajig sizes`

- 설치된 모든 패키지의 버전 및 배포 목록:

`wajig versions`

- 업그레이드 가능한 패키지의 버전 목록:

`wajig toupgrade`

- 주어진 패키지에 대한 의존성을 가진 패키지 표시:

`wajig dependents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
