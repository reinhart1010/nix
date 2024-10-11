---
layout: page
title: common/cupsaccept (한국어)
description: "목적지로 전송된 작업을 수락."
content_hash: 5cf6ae8b547c3302e175f2a8959d79848bd6d5dd
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/cupsaccept.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cupsaccept.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsaccept.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsaccept

목적지로 전송된 작업을 수락.
참고: 목적지는 프린터 또는 프린터 클래스라고 함.
추가 정보: `cupsreject`, `cupsenable`, `cupsdisable`, `lpstat`.
더 많은 정보: <https://www.cups.org/doc/man-cupsaccept.html>.

- 지정된 목적지로 인쇄 작업 수락:

`cupsaccept `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지1 목적지2 ...</span>

- 다른 서버 지정:

`cupsaccept -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지1 목적지2 ...</span>
