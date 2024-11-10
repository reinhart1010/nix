---
layout: page
title: linux/ip-rule (한국어)
description: "IP 라우팅 정책 데이터베이스 관리."
content_hash: 4943a316a6a22329866a043ca54f672d54f720c7
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ip-rule.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/ip-rule.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ip rule

IP 라우팅 정책 데이터베이스 관리.
더 많은 정보: <https://manned.org/ip-rule>.

- 라우팅 정책 표시:

`ip rule `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">show|list</span>

- 패킷 소스 주소를 기준으로 새 규칙 추가:

`sudo ip rule add from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- 패킷 목적지 주소를 기준으로 새 규칙 추가:

`sudo ip rule add to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- 패킷 소스 주소를 기준으로 규칙 삭제:

`sudo ip rule delete from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- 패킷 목적지 주소를 기준으로 규칙 삭제:

`sudo ip rule delete to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2/32</span>

- 삭제된 모든 규칙 플러시:

`ip rule flush`

- 모든 규칙을 파일에 저장:

`ip rule save > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/ip_규칙들.dat</span>

- 파일에서 모든 규칙 복원:

`ip rule restore < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/ip_규칙들.dat</span>
