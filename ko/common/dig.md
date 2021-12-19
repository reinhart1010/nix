---
layout: page
title: common/dig (한국어)
description: "DNS 조회 유틸리티."
content_hash: 52dba3b0b1ea5f5c19e08c8844b12de223140b15
related_topics:
  - title: English version
    url: /en/common/dig.html
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
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dig

DNS 조회 유틸리티.
더 많은 정보: <https://manpages.debian.org/dnsutils/dig.1.html>.

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
