---
layout: page
title: sunos/devfsadm (한국어)
description: "`/dev`의 관리 명령어입니다. `/dev` 네임스페이스를 유지합니다."
content_hash: 941b13a382bd5b18973b444557d79d9613709158
last_modified_at: 2024-06-24
related_topics:
  - title: English version
    url: /en/sunos/devfsadm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/devfsadm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/devfsadm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/sunos/devfsadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/devfsadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/devfsadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# devfsadm

`/dev`의 관리 명령어입니다. `/dev` 네임스페이스를 유지합니다.
더 많은 정보: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- 새 디스크 검색:

`devfsadm -c disk`

- 미해결된 /dev 링크를 정리하고 새 장치를 검색:

`devfsadm -C -v`

- 시뮬레이션 실행 - 변경될 내용을 출력하지만 수정하지 않음:

`devfsadm -C -v -n`
