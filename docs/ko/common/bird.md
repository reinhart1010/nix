---
layout: page
title: common/bird (한국어)
description: "BIRD 인터넷 라우팅 데몬."
content_hash: f8a6d795b944eb775bb83720946ea1c3f6746d45
last_modified_at: 2024-09-21
related_topics:
  - title: Deutsch version
    url: /de/common/bird.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bird.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bird.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bird.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bird

BIRD 인터넷 라우팅 데몬.
BGP, OSPF, Babel 등을 지원하는 라우팅 데몬.
더 많은 정보: <https://bird.network.cz/>.

- 특정 구성 파일로 Bird를 시작:

`bird -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bird.conf</span>

- 특정 사용자 및 그룹으로 Bird를 시작:

`bird -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>
