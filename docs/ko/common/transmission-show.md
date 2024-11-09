---
layout: page
title: common/transmission-show (한국어)
description: "토렌트 파일에 대한 정보 가져오기."
content_hash: cce87d18d209498bcfe9422d553e25e4975615ac
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/transmission-show.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-show.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/transmission-show.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/transmission-show.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># transmission-show

토렌트 파일에 대한 정보 가져오기.
같이 보기: `transmission`.
더 많은 정보: <https://manned.org/transmission-show>.

- 특정 토렌트의 메타데이터 표시:

`transmission-show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.torrent</span>

- 특정 토렌트에 대한 마그넷 링크 생성:

`transmission-show --magnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.torrent</span>

- 토렌트의 트래커를 조회하고 현재 피어 수 출력:

`transmission-show --scrape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.torrent</span>
