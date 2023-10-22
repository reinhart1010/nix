---
layout: page
title: linux/add-apt-repository (한국어)
description: "적절한 저장소 정의를 관리합니다."
content_hash: 78e3b6491c0c2e097de22a7d9a84c95bb0b19d99
last_modified_at: 2023-10-22
related_topics:
  - title: català version
    url: /ca/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/add-apt-repository.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/add-apt-repository.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># add-apt-repository

적절한 저장소 정의를 관리합니다.
더 많은 정보: <https://manned.org/apt-add-repository>.

- 새로운 apt 레포지토리 추가:

`add-apt-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_스펙</span>

- apt 레포지토리 삭제:

`add-apt-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_스펙</span>

- 저장소 추가 후 패키지 캐시 업데이트:

`add-apt-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_스펙</span>

- 저장소에서 소스 패키지를 다운로드하도록 허용:

`add-apt-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_스펙</span>
