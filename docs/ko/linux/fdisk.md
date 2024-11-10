---
layout: page
title: linux/fdisk (한국어)
description: "하드 디스크의 파티션 테이블과 파티션을 관리합니다."
content_hash: a2d9bf0fa4635f4601fc22ad5b3b1836edae5443
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/fdisk.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/fdisk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/fdisk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/fdisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fdisk

하드 디스크의 파티션 테이블과 파티션을 관리합니다.
같이 보기: `partprobe`.
더 많은 정보: <https://manned.org/fdisk>.

- 파티션 나열:

`sudo fdisk -l`

- 파티션 조작기 시작:

`sudo fdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- 디스크 파티션 중, 파티션 생성:

`n`

- 디스크 파티션 중, 삭제할 파티션 선택:

`d`

- 디스크 파티션 중, 파티션 테이블 보기:

`p`

- 디스크 파티션 중, 변경사항 저장:

`w`

- 디스크 파티션 중, 변경사항 취소:

`q`

- 디스크 파티션 중, 도움말 메뉴 열기:

`m`
