---
layout: page
title: linux/vmstat (한국어)
description: "프로세스, 메모리, 페이징, 블록 IO, 트랩, 디스크 및 CPU 활동에 대한 정보를 표시합니다."
content_hash: 769a9fd3ceef914d2971c31a4700cca28653b15e
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/vmstat.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/vmstat.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/vmstat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vmstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vmstat

프로세스, 메모리, 페이징, 블록 IO, 트랩, 디스크 및 CPU 활동에 대한 정보를 표시합니다.
더 많은 정보: <https://manned.org/vmstat>.

- 가상 메모리 통계를 표시:

`vmstat`

- 2초마다 5회 보고서 표시:

`vmstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
