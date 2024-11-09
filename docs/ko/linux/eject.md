---
layout: page
title: linux/eject (한국어)
description: "CD, 플로피 디스크 및 테이프 드라이브를 꺼냅니다."
content_hash: 88b48e9a9bcb67762f267cde7f9a3ea649a0f5a6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/eject.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/eject.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eject

CD, 플로피 디스크 및 테이프 드라이브를 꺼냅니다.
더 많은 정보: <https://manned.org/eject>.

- 기본 장치 표시:

`eject -d`

- 기본 장치 꺼내기:

`eject`

- 특정 장치 꺼내기 (기본 순서는 cd-rom, scsi, 플로피 및 테이프입니다):

`eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- 장치 트레이가 열려 있는지 닫혀 있는지 토글:

`eject -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- CD 드라이브 꺼내기:

`eject -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/cdrom</span>

- 플로피 드라이브 꺼내기:

`eject -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/floppy</span>

- 테이프 드라이브 꺼내기:

`eject -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/mnt/tape</span>
