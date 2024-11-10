---
layout: page
title: linux/named (한국어)
description: "DNS(동적 이름 서비스) 서버 데몬을 실행하여 호스트명을 IP 주소로, 그 반대로 변환합니다."
content_hash: cb77939fc5ffda5c453fdf57a5417babc44f4dae
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/named.html
    icon: bi bi-globe
tldri18n_status: 2
---
# named

DNS(동적 이름 서비스) 서버 데몬을 실행하여 호스트명을 IP 주소로, 그 반대로 변환합니다.
더 많은 정보: <https://manned.org/named>.

- 기본 구성 파일 `/etc/named.conf`를 읽고 초기 데이터를 읽은 후 쿼리를 수신:

`named`

- 사용자 지정 구성 파일 읽기:

`named -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/named.conf</span>

- 호스트 머신이 다른 프로토콜을 사용할 수 있어도 IPv4 또는 IPv6만 사용:

`named `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-4|-6</span>

- 기본 포트 53 대신 특정 포트에서 쿼리를 수신:

`named -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 포그라운드에서 서버를 실행하고 데몬화하지 않음:

`named -f`
