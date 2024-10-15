---
layout: page
title: linux/mkfs.cramfs (한국어)
description: "파티션 내에 ROM 파일 시스템 생성."
content_hash: a0870fb1c539b06673a2b3c79d34b5660b548eed
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/mkfs.cramfs.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mkfs.cramfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.cramfs

파티션 내에 ROM 파일 시스템 생성.
더 많은 정보: <https://manned.org/mkfs.cramfs>.

- 장치 b의 파티션 1 (`sdb1`) 에 ROM 파일 시스템 생성:

`mkfs.cramfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 볼륨 이름을 지정하여 ROM 파일 시스템 생성:

`mkfs.cramfs -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
