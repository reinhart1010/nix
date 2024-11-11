---
layout: page
title: linux/spi (한국어)
description: "패키지와 슬랙빌드를 모두 관리하는 메타 패키지 관리자."
content_hash: a949c8987565cd94a71304b64d9cf7c025bdeb22
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/spi.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/spi.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># spi

패키지와 슬랙빌드를 모두 관리하는 메타 패키지 관리자.
더 많은 정보: <https://github.com/gapan/spi>.

- 사용 가능한 패키지와 슬랙빌드 목록 업데이트:

`spi --update`

- 패키지 또는 슬랙빌드 설치:

`spi --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지/슬랙빌드_이름</span>

- 설치된 모든 패키지를 최신 버전으로 업그레이드:

`spi --upgrade`

- 패키지 이름 또는 설명으로 패키지나 슬랙빌드 찾기:

`spi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>

- 패키지 또는 슬랙빌드에 대한 정보 표시:

`spi --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지/슬랙빌드_이름</span>

- 로컬 패키지 및 슬랙빌드 캐시 정리:

`spi --clean`
