---
layout: page
title: linux/apk (한국어)
description: "Alpine Linux 패키지 관리 도구."
content_hash: dbfaf2ab0fed7929bec46d8ac7fe0b660deb5042
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/linux/apk.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apk.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apk.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apk.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apk

Alpine Linux 패키지 관리 도구.
더 많은 정보: <https://manned.org/apk>.

- 모든 원격 저장소에서 저장소 색인 업데이트:

`apk update`

- 새 패키지 설치:

`apk add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거:

`apk del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지를 복구하거나 주요 의존성을 수정하지 않고 업그레이드:

`apk fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 키워드를 통해 패키지 검색:

`apk search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- 특정 패키지에 대한 정보 표시:

`apk info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
