---
layout: page
title: common/drill (한국어)
description: "다양한 DNS 쿼리를 수행."
content_hash: c1cacb6d797e87045e209c1934c9eb9feb50c300
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/drill.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/drill.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/drill.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/drill.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># drill

다양한 DNS 쿼리를 수행.
더 많은 정보: <https://manned.org/drill>.

- 호스트 이름 (A 레코드)과 연결된 IP를 조회:

`drill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 특정 도메인 이름 (MX 레코드)과 연결된 메일 서버를 조회:

`drill mx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 특정 도메인 이름에 대한 모든 유형의 레코드를 가져옴:

`drill any `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 쿼리할 대체 DNS 서버를 지정:

`drill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- IP 주소 (PTR 레코드)에 대해 역방향 DNS 조회를 수행:

`drill -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- 루트 서버부터 도메인 이름까지 DNSSEC 추적을 수행:

`drill -TD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 도메인 이름에 대한 DNSKEY 레코드 표시:

`drill -s dnskey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
