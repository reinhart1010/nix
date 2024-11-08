---
layout: page
title: linux/apt-mark (한국어)
description: "설치된 패키지의 상태를 변경하는 유틸리티."
content_hash: c66750ffa3b1834be492ffb5064dda80acfb5418
last_modified_at: 2024-11-08
related_topics:
  - title: català version
    url: /ca/linux/apt-mark.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-mark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-mark.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-mark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-mark.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-mark.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-mark.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apt-mark.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apt-mark

설치된 패키지의 상태를 변경하는 유틸리티.
더 많은 정보: <https://manned.org/apt-mark.8>.

- 패키지를 자동 설치로 표시:

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지를 현재 버전으로 고정하고 업데이트 방지:

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지를 다시 업데이트 가능하도록 허용:

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 수동으로 설치된 패키지 표시:

`apt-mark showmanual`

- 업데이트되지 않는 고정된 패키지 표시:

`apt-mark showhold`
