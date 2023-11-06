---
layout: page
title: common/nc (한국어)
description: "Netcat은 TCP 또는 UDP 데이터 작업을 위한 다목적 유틸리티입니다."
content_hash: c995356385a8c519eca7be5d3a474df439eee4f3
last_modified_at: 2023-11-06
related_topics:
  - title: English version
    url: /en/common/nc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nc.html
    icon: bi bi-globe
---
# nc

Netcat은 TCP 또는 UDP 데이터 작업을 위한 다목적 유틸리티입니다.
더 많은 정보: <https://manned.org/man/nc.1>.

- 특정 포트에서 수신대기 및 수신한 데이터 출력:

`nc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 특정 포트에 연결:

`nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 타임아웃 설정:

`nc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타임아웃_될_시간</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 클라이언트가 연결 해제 된 상황에도 서버를 가동 상태로 유지:

`nc -k -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- EOF가 들어와도 클라이언트와 연결 유지:

`nc -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타임아웃_될_시간</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>

- 특정 호스트의 포트가 열렸는지 확인:

`nc -v -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 프록시처럼 로컬 TCP 포트로부터 받은 데이터를 주어진 원격 호스트에게 전달합니다:

`nc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로컬_포트</span>` | nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_포트</span>
