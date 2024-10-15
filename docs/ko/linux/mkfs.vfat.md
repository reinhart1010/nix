---
layout: page
title: linux/mkfs.vfat (한국어)
description: "파티션 내에 MS-DOS 파일 시스템 생성."
content_hash: 8f96b8426cb6a6e678059df0d989841e87606750
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/mkfs.vfat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mkfs.vfat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.vfat

파티션 내에 MS-DOS 파일 시스템 생성.
더 많은 정보: <https://manned.org/mkfs.vfat>.

- 장치 b의 파티션 1 (`sdb1`) 에 vfat 파일 시스템 생성:

`mkfs.vfat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 볼륨 이름과 함께 파일 시스템 생성:

`mkfs.vfat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 볼륨 ID와 함께 파일 시스템 생성:

`mkfs.vfat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 2 대신 5개의 파일 할당 테이블 사용:

`mkfs.vfat -f 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
