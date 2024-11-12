---
layout: page
title: osx/nettop (한국어)
description: "네트워크에 대한 업데이트된 정보를 표시합니다."
content_hash: 69ac023cd7982f1302e8fa9c5dca9a0b41bedf5d
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/nettop.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/nettop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nettop

네트워크에 대한 업데이트된 정보를 표시합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/nettop.1.html>.

- 모든 인터페이스의 TCP 및 UDP 소켓 모니터링:

`nettop`

- 루프백 인터페이스의 TCP 소켓 모니터링:

`nettop -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">loopback</span>

- 특정 프로세스 모니터링:

`nettop -p "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_ID|프로세스_이름</span>`"`

- 프로세스별 요약 표시:

`nettop -P`

- 네트워크 정보의 10개의 샘플 출력:

`nettop -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 5초마다 변경 사항 모니터링:

`nettop -d -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- nettop 실행 중 상호작용 명령 나열:

`h`

- 도움말 표시:

`nettop -h`
