---
layout: page
title: osx/diskutil (한국어)
description: "로컬 디스크 및 볼륨을 관리하는 유틸리티."
content_hash: 1e0b1e9342ccd864d05fa3715605ae786d2268d3
last_modified_at: 2024-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/diskutil.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/diskutil.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/diskutil.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/diskutil.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/diskutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/diskutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diskutil

로컬 디스크 및 볼륨을 관리하는 유틸리티.
`partitiondisk`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- 현재 사용 가능한 모든 디스크, 파티션 및 마운트된 볼륨 나열:

`diskutil list`

- 볼륨의 파일 시스템 데이터 구조 복구:

`diskutil repairVolume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/디스크_장치</span>

- 볼륨 마운트 해제:

`diskutil unmountDisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/디스크_장치</span>

- CD/DVD 꺼내기 (먼저 마운트 해제 필요):

`diskutil eject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/디스크_장치1</span>
