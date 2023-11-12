---
layout: page
title: common/dig (한국어)
description: "DNS 조회 유틸리티."
content_hash: a1996d3d98c670bb48e83a83188fe33055c0486a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dig.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/dig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dig.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dig

DNS 조회 유틸리티.
더 많은 정보: <https://manned.org/dig>.

- 호스트이름과 관련된 IP 조회하기 (A records):

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 주어진 도메인 이름과 관련된 메일 서버 조회하기 (MX record):

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` MX`

- 주어진 도메인 이름에 대한 모든 유형의 레코드들 가져오기:

`dig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` ANY`

- 쿼리할 대체 DNS 서버를 지정하기:

`dig @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- IP 주소에서 역방향 DNS 조회하기 (PTR record):

`dig -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- 영역에 대해 권한있는 이름 서버들을 찾고 SOA 레코드들 표시하기:

`dig +nssearch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 반복적인 쿼리들을 수행하고 도메인 이름을 분석하기 위해 전체 추적 경로를 표시하기:

`dig +trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
