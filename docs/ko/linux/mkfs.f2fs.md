---
layout: page
title: linux/mkfs.f2fs (한국어)
description: "파티션 내에 F2FS 파일 시스템 생성."
content_hash: 4672ce3eedf6c0bc2b120f0e76971b5af9d4ab89
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/mkfs.f2fs.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/mkfs.f2fs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mkfs.f2fs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.f2fs

파티션 내에 F2FS 파일 시스템 생성.
더 많은 정보: <https://manned.org/mkfs.f2fs>.

- 장치 b의 파티션 1 (`sdb1`) 에 F2FS 파일 시스템 생성:

`sudo mkfs.f2fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 볼륨 레이블을 지정하여 F2FS 파일 시스템 생성:

`sudo mkfs.f2fs -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_레이블</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
