---
layout: page
title: linux/htpdate (한국어)
description: "웹 서버의 HTTP 헤더를 통해 로컬 날짜 및 시간을 동기화합니다."
content_hash: 341ffe185afd17f6dde5433ee5c1fcfca74b4550
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/htpdate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/htpdate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># htpdate

웹 서버의 HTTP 헤더를 통해 로컬 날짜 및 시간을 동기화합니다.
더 많은 정보: <https://www.vervest.org/htp/>.

- 날짜와 시간 동기화:

`sudo htpdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 동기화 시뮬레이션 수행, 실제 동작은 없음:

`htpdate -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 체계적인 시계 드리프트 보정:

`sudo htpdate -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 동기화 후 즉시 시간 설정:

`sudo htpdate -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>
