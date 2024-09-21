---
layout: page
title: common/bandwhich (한국어)
description: "프로세스, 연결 또는 원격 IP/호스트 이름별로 현재 네트워크 사용량을 표시."
content_hash: fb60ccf7d7b25f1eeec5589d88c8d0a1c9d7a00d
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bandwhich.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bandwhich.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bandwhich

프로세스, 연결 또는 원격 IP/호스트 이름별로 현재 네트워크 사용량을 표시.
더 많은 정보: <https://github.com/imsnif/bandwhich>.

- 원격 주소 테이블만 표시:

`bandwhich --addresses`

- DNS 쿼리 표시:

`bandwhich --show-dns`

- 총 (누적) 사용량 표시:

`bandwhich --total-utilization`

- 특정 네트워크 인터페이스에 대한 네트워크 활용도를 표시:

`bandwhich --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 특정 DNS 서버로 DNS 쿼리를 표시:

`bandwhich --show-dns --dns-server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns_서버_ip</span>
