---
layout: page
title: linux/dumpe2fs (한국어)
description: "ext2/ext3/ext4 파일시스템의 슈퍼블록 및 블록 그룹 정보를 출력합니다."
content_hash: f9c2d6cdb04fa9d4df5acc3f3d0244a3b47b231a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/dumpe2fs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dumpe2fs

ext2/ext3/ext4 파일시스템의 슈퍼블록 및 블록 그룹 정보를 출력합니다.
`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">장치</span>를 사용하여 이 명령을 실행하기 전에 파티션을 마운트 해제하세요.
더 많은 정보: <https://manned.org/dumpe2fs>.

- ext2, ext3 및 ext4 파일시스템 정보 표시:

`dumpe2fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 파일시스템에서 불량으로 예약된 블록 표시:

`dumpe2fs -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 인식할 수 없는 기능 플래그가 있어도 파일시스템 정보를 강제로 표시:

`dumpe2fs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 슈퍼블록 정보만 표시하고 블록 그룹 설명자 세부 정보는 표시하지 않음:

`dumpe2fs -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 그룹의 세부 정보 블록 번호를 16진수 형식으로 출력:

`dumpe2fs -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
