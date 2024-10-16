---
layout: page
title: common/dog (한국어)
description: "DNS 조회 유틸리티."
content_hash: 8da74f44e27ce185bc5f38d99e65f2b2cb8b6efd
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/dog.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/dog.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dog.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dog

DNS 조회 유틸리티.
다채로운 출력을 제공하고, DNS-over-TLS 및 DNS-over-HTTPS 프로토콜을 지원하며, JSON을 내보낼 수 있음.
더 많은 정보: <https://dns.lookup.dog>.

- 호스트 이름과 연결된 IP를 조회 (A 레코드):

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 특정 도메인 이름과 관련된 MX 레코드 유형을 쿼리:

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` MX`

- 쿼리할 특정 DNS 서버를 지정 (예. Cloudflare):

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` MX @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>

- UDP가 아닌 TCP를 통한 쿼리:

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` MX @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>` --tcp`

- 명시적 인수를 사용하여 TCP를 통해 특정 도메인 이름과 연결된 MX 레코드 유형을 쿼리:

`dog --query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --type MX --nameserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>` --tcp`

- DoH(DNS over HTTPS)를 사용하여 호스트 이름(A 레코드)과 연견된 IP를 조회:

`dog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --https @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://cloudflare-dns.com/dns-query</span>
