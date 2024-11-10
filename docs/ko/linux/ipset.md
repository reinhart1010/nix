---
layout: page
title: linux/ipset (한국어)
description: "방화벽 규칙을 위한 IP 집합 생성."
content_hash: c24195d0933887ace5a3e1c4c96415f62ae58dfe
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ipset.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ipset

방화벽 규칙을 위한 IP 집합 생성.
더 많은 정보: <https://manned.org/ipset>.

- IP 주소를 포함할 빈 IP 집합 생성:

`ipset create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">집합_이름</span>` hash:ip`

- 특정 IP 집합 삭제:

`ipset destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">집합_이름</span>

- 특정 집합에 IP 주소 추가:

`ipset add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">집합_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.25</span>

- 집합에서 특정 IP 주소 삭제:

`ipset del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">집합_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.25</span>

- IP 집합 저장:

`ipset save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">집합_이름</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/ip_집합</span>
