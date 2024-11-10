---
layout: page
title: linux/iostat (한국어)
description: "장치 및 파티션에 대한 통계 보고."
content_hash: 3b8e6d7ce1f256fd776044740ecdc1e666a1abfd
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/iostat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/iostat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# iostat

장치 및 파티션에 대한 통계 보고.
더 많은 정보: <https://manned.org/iostat>.

- 시스템 시작 이후의 CPU 및 디스크 통계 보고서 표시:

`iostat`

- 단위를 메가바이트로 변환한 CPU 및 디스크 통계 보고서 표시:

`iostat -m`

- CPU 통계 표시:

`iostat -c`

- 디스크 이름(및 LVM 포함)을 사용한 디스크 통계 표시:

`iostat -N`

- 장치 "sda"에 대한 디스크 이름을 포함한 확장 디스크 통계 표시:

`iostat -xN `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sda</span>

- 2초마다 CPU 및 디스크 통계의 증분 보고서 표시:

`iostat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>
