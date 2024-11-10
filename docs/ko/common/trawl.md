---
layout: page
title: common/trawl (한국어)
description: "네트워크 인터페이스 정보를 콘솔에 출력하는 도구로, ifconfig/ipconfig/ip/ifdata와 유사합니다."
content_hash: c0a2fb417e4a368f9ba1f78037573dd2a0e896da
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/trawl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trawl

네트워크 인터페이스 정보를 콘솔에 출력하는 도구로, ifconfig/ipconfig/ip/ifdata와 유사합니다.
더 많은 정보: <https://github.com/robphoenix/trawl>.

- 열 이름 표시:

`trawl -n`

- 대소문자 구분 없는 정규 표현식을 사용하여 인터페이스 이름 필터링:

`trawl -f wi`

- 사용 가능한 인터페이스 나열:

`trawl -i`

- 루프백 인터페이스 포함:

`trawl -l`
