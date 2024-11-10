---
layout: page
title: linux/vgscan (한국어)
description: "지원되는 모든 논리 볼륨 관리자(LVM) 블록 장치에서 볼륨 그룹을 검색합니다."
content_hash: 53c1d5e2fa324c8af9b5b3c7c1a2ee085d303b40
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/vgscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vgscan

지원되는 모든 논리 볼륨 관리자(LVM) 블록 장치에서 볼륨 그룹을 검색합니다.
같이 보기: `lvm`, `vgchange`.
더 많은 정보: <https://manned.org/vgscan>.

- 볼륨 그룹을 검색하고 발견된 각 그룹에 대한 정보 표시:

`sudo vgscan`

- 볼륨 그룹을 검색하고 발견된 그룹의 논리 볼륨에 접근하는 데 필요한 `/dev`의 특별 파일이 이미 존재하지 않으면 추가:

`sudo vgscan --mknodes`
