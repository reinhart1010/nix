---
layout: page
title: osx/netstat (한국어)
description: "네트워크 연결, 열린 소켓 포트 등 네트워크 관련 정보를 표시합니다."
content_hash: 4b12c7f8b02acc0f3c19d5bb0176cfcebbcf2a6a
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/netstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/netstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netstat

네트워크 연결, 열린 소켓 포트 등 네트워크 관련 정보를 표시합니다.
같이 보기: 네트워크 연결(리스닝 포트 포함)을 나열하려면 `lsof`를 참조하세요.
더 많은 정보: <https://keith.github.io/xcode-man-pages/netstat.1.html>.

- 특정 프로토콜을 수신 중인 PID와 프로그램 이름 표시:

`netstat -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로토콜</span>

- 라우팅 테이블을 출력하고 IP 주소를 호스트명으로 해석하지 않음:

`netstat -nr`

- IPv4 주소의 라우팅 테이블 출력:

`netstat -nr -f inet`
