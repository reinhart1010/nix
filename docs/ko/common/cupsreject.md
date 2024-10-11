---
layout: page
title: common/cupsreject (한국어)
description: "프린터로 전송된 작업 거부."
content_hash: fbd547ef0d629c9108b9d34945f8a1a3494b2b8a
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/cupsreject.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cupsreject.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsreject.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsreject

프린터로 전송된 작업 거부.
참고: 목적지는 프린터 또는 프린터 클래스를 나타냄.
더 보기: `cupsaccept`, `cupsenable`, `cupsdisable`, `lpstat`.
더 많은 정보: <https://www.cups.org/doc/man-cupsaccept.html>.

- 지정된 목적지로의 인쇄 작업 거부:

`cupsreject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지1 목적지2 ...</span>

- 다른 서버 지정:

`cupsreject -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지1 목적지2 ...</span>

- 이유 문자열을 지정 (기본적으로 "Reason Unknown"):

`cupsreject -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이유</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지1 목적지2 ...</span>
