---
layout: page
title: linux/apt-add-repository (한국어)
description: "`apt` 저장소 정의를 관리합니다."
content_hash: bc1e765a007c45e0ba640926895f6fc5772bfa9c
last_modified_at: 2024-11-08
related_topics:
  - title: català version
    url: /ca/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-add-repository.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-add-repository.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apt-add-repository.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apt-add-repository

`apt` 저장소 정의를 관리합니다.
더 많은 정보: <https://manned.org/apt-add-repository.1>.

- 새 `apt` 저장소 추가:

`apt-add-repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_명세</span>

- `apt` 저장소 제거:

`apt-add-repository --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_명세</span>

- 저장소 추가 후 패키지 캐시 업데이트:

`apt-add-repository --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_명세</span>

- 소스 패키지 활성화:

`apt-add-repository --enable-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_명세</span>
