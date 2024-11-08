---
layout: page
title: linux/conntrack (한국어)
description: "Netfilter 연결 추적 시스템과 상호작용합니다."
content_hash: 23220fc11d075dfcdb8a666d4d673453f88ce729
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/conntrack.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/conntrack.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># conntrack

Netfilter 연결 추적 시스템과 상호작용합니다.
연결 흐름을 검색, 나열, 검사, 수정 및 삭제합니다.
더 많은 정보: <https://manned.org/conntrack>.

- 현재 추적 중인 모든 연결 나열:

`conntrack --dump`

- 연결 변경 사항의 실시간 이벤트 로그 표시:

`conntrack --event`

- 연결 변경 사항 및 관련 타임스탬프의 실시간 이벤트 로그 표시:

`conntrack --event -o timestamp`

- 특정 IP 주소에 대한 연결 변경 사항의 실시간 이벤트 로그 표시:

`conntrack --event --orig-src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>

- 특정 소스 IP 주소에 대한 모든 흐름 삭제:

`conntrack --delete --orig-src `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>
