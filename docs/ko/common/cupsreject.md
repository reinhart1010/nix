---
layout: page
title: common/cupsreject (한국어)
description: "프린터로 전송된 작업 거부."
content_hash: fbd547ef0d629c9108b9d34945f8a1a3494b2b8a
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/cupsreject.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cupsreject.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsreject

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
