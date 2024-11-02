---
layout: page
title: common/kdig (한국어)
description: "고급 DNS 조회 유틸리티."
content_hash: fb24a9506ae3197f478cd9e9763921a0a8481282
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/kdig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kdig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kdig

고급 DNS 조회 유틸리티.
더 많은 정보: <https://www.knot-dns.cz/docs/latest/html/man_kdig.html>.

- 호스트 이름과 연결된 IP(A 레코드) 조회:

`kdig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 특정 DNS 서버를 지정하여 쿼리(예: Google DNS):

`kdig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- 주어진 도메인 이름과 연결된 특정 DNS 레코드 유형 쿼리:

`kdig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|AAAA|NS|SOA|DNSKEY|ANY</span>

- DNS over TLS(DoT)를 사용하여 호스트 이름과 연결된 IP(A 레코드) 조회:

`kdig -d @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` +tls-ca +tls-host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns.google</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- DNS over HTTPS(DoH)를 사용하여 호스트 이름과 연결된 IP(A 레코드) 조회:

`kdig -d @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1</span>` +https +tls-hostname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1dot1dot1dot1.cloudflare-dns.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
