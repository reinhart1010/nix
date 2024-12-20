---
layout: page
title: common/host (한국어)
description: "도메인 네임 서버 조회."
content_hash: 25c2b12953a1b38ea00480cc9599d525cf4aab17
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/host.html
    icon: bi bi-globe
tldri18n_status: 2
---
# host

도메인 네임 서버 조회.
더 많은 정보: <https://manned.org/host>.

- 도메인의 A, AAAA 및 MX 레코드 조회:

`host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>

- 도메인의 필드 (CNAME, TXT, ...) 조회:

`host -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>

- IP 역방향 조회:

`host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>

- 쿼리할 대체 DNS 서버를 지정:

`host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>
