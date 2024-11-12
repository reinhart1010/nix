---
layout: page
title: osx/tmutil (한국어)
description: "Time Machine 백업을 관리하는 도구. 대부분의 동사는 루트 권한이 필요합니다."
content_hash: 3fb1a3375a4c8a428015fb0224fc93aa28cd2cd3
last_modified_at: 2024-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/tmutil.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/tmutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/tmutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tmutil

Time Machine 백업을 관리하는 도구. 대부분의 동사는 루트 권한이 필요합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/tmutil.8.html>.

- HFS+ 드라이브를 백업 대상으로 설정:

`sudo tmutil setdestination `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디스크_마운트_포인트</span>

- APF 공유 또는 SMB 공유를 백업 대상으로 설정:

`sudo tmutil setdestination "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로토콜://사용자[:비밀번호]@호스트/공유</span>`"`

- 주어진 대상을 목적지 목록에 추가:

`sudo tmutil setdestination -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상</span>

- 자동 백업 활성화:

`sudo tmutil enable`

- 자동 백업 비활성화:

`sudo tmutil disable`

- 백업이 실행 중이 아니라면 시작하고 셸의 제어를 해제:

`sudo tmutil startbackup`

- 백업을 시작하고 완료될 때까지 대기:

`sudo tmutil startbackup -b`

- 백업 중지:

`sudo tmutil stopbackup`
